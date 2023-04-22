from django.shortcuts import redirect
from google.oauth2 import credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

class GoogleCalendarInitView(APIView):
    def get(self, request, format=None):
        SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
        flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
        flow.redirect_uri = 'http://localhost:8000/rest/v1/calendar/redirect/'

        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true'
        )

        request.session['state'] = state

        return redirect(authorization_url)
class GoogleCalendarRedirectView(APIView):
    def get(self, request, format=None):
        flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES, state=request.session['state'])
        flow.redirect_uri = 'http://localhost:8000/rest/v1/calendar/redirect/'

        authorization_response = request.build_absolute_uri()
        flow.fetch_token(authorization_response=authorization_response)

        credentials = flow.credentials
        service = build('calendar', 'v3', credentials=credentials)

        events_result = service.events().list(calendarId='primary', maxResults=10, singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])

        return render(request, 'calendar.html', {'events': events})