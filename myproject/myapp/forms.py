# myapp/forms.py
from django import forms
from .models import MyModel

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'last_flag']

    # Define your form fields here
    duration = forms.FloatField(label='Duration')
    protocol_type = forms.CharField(label='Protocol Type', max_length=255)
    service = forms.CharField(label='Service', max_length=255)
    flag = forms.CharField(label='Flag', max_length=255)
    src_bytes = forms.FloatField(label='Source Bytes')
    dst_bytes = forms.FloatField(label='Destination Bytes')
    land = forms.BooleanField(label='Land')
    wrong_fragment = forms.FloatField(label='Wrong Fragment')
    urgent = forms.FloatField(label='Urgent')
    hot = forms.FloatField(label='Hot')
    num_failed_logins = forms.FloatField(label='Number of Failed Logins')
    logged_in = forms.BooleanField(label='Logged In')
    num_compromised = forms.FloatField(label='Number of Compromised')
    root_shell = forms.BooleanField(label='Root Shell')
    su_attempted = forms.BooleanField(label='SU Attempted')
    num_root = forms.FloatField(label='Number of Root')
    num_file_creations = forms.FloatField(label='Number of File Creations')
    num_shells = forms.FloatField(label='Number of Shells')
    num_access_files = forms.FloatField(label='Number of Access Files')
    num_outbound_cmds = forms.FloatField(label='Number of Outbound Commands')
    is_host_login = forms.BooleanField(label='Is Host Login')
    is_guest_login = forms.BooleanField(label='Is Guest Login')
    count = forms.FloatField(label='Count')
    srv_count = forms.FloatField(label='Service Count')
    serror_rate = forms.FloatField(label='Serror Rate')
    srv_serror_rate = forms.FloatField(label='Service Serror Rate')
    rerror_rate = forms.FloatField(label='Rerror Rate')
    srv_rerror_rate = forms.FloatField(label='Service Rerror Rate')
    same_srv_rate = forms.FloatField(label='Same Service Rate')
    diff_srv_rate = forms.FloatField(label='Different Service Rate')
    srv_diff_host_rate = forms.FloatField(label='Service Different Host Rate')
    dst_host_count = forms.FloatField(label='Destination Host Count')
    dst_host_srv_count = forms.FloatField(label='Destination Host Service Count')
    dst_host_same_srv_rate = forms.FloatField(label='Destination Host Same Service Rate')
    dst_host_diff_srv_rate = forms.FloatField(label='Destination Host Different Service Rate')
    dst_host_same_src_port_rate = forms.FloatField(label='Destination Host Same Source Port Rate')
    dst_host_srv_diff_host_rate = forms.FloatField(label='Destination Host Service Different Host Rate')
    dst_host_serror_rate = forms.FloatField(label='Destination Host Serror Rate')
    dst_host_srv_serror_rate = forms.FloatField(label='Destination Host Service Serror Rate')
    dst_host_rerror_rate = forms.FloatField(label='Destination Host Rerror Rate')
    dst_host_srv_rerror_rate = forms.FloatField(label='Destination Host Service Rerror Rate')
    last_flag = forms.FloatField(label='Last Flag')
