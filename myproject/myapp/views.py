# myapp/views.py
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from .forms import MyModelForm
def predict_ml(data):
    prediction_result = "ML Prediction Result"
    return prediction_result
def success_view(request):
    return render(request, 'myapp/success.html')
def my_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            data = {
                'duration': form.cleaned_data['duration'],
                'protocol_type': form.cleaned_data['protocol_type'],
                'service': form.cleaned_data['service'],
                'flag': form.cleaned_data['flag'],
                'src_bytes': form.cleaned_data['src_bytes'],
                'dst_bytes': form.cleaned_data['dst_bytes'],
                'land': form.cleaned_data['land'],
                'wrong_fragment': form.cleaned_data['wrong_fragment'],
                'urgent': form.cleaned_data['urgent'],
                'hot': form.cleaned_data['hot'],
                'num_failed_logins': form.cleaned_data['num_failed_logins'],
                'logged_in': form.cleaned_data['logged_in'],
                'num_compromised': form.cleaned_data['num_compromised'],
                'root_shell': form.cleaned_data['root_shell'],
                'su_attempted': form.cleaned_data['su_attempted'],
                'num_root': form.cleaned_data['num_root'],
                'num_file_creations': form.cleaned_data['num_file_creations'],
                'num_shells': form.cleaned_data['num_shells'],
                'num_access_files': form.cleaned_data['num_access_files'],
                'num_outbound_cmds': form.cleaned_data['num_outbound_cmds'],
                'is_host_login': form.cleaned_data['is_host_login'],
                'is_guest_login': form.cleaned_data['is_guest_login'],
                'count': form.cleaned_data['count'],
                'srv_count': form.cleaned_data['srv_count'],
                'serror_rate': form.cleaned_data['serror_rate'],
                'srv_serror_rate': form.cleaned_data['srv_serror_rate'],
                'rerror_rate': form.cleaned_data['rerror_rate'],
                'srv_rerror_rate': form.cleaned_data['srv_rerror_rate'],
                'same_srv_rate': form.cleaned_data['same_srv_rate'],
                'diff_srv_rate': form.cleaned_data['diff_srv_rate'],
                'srv_diff_host_rate': form.cleaned_data['srv_diff_host_rate'],
                'dst_host_count': form.cleaned_data['dst_host_count'],
                'dst_host_srv_count': form.cleaned_data['dst_host_srv_count'],
                'dst_host_same_srv_rate': form.cleaned_data['dst_host_same_srv_rate'],
                'dst_host_diff_srv_rate': form.cleaned_data['dst_host_diff_srv_rate'],
                'dst_host_same_src_port_rate': form.cleaned_data['dst_host_same_src_port_rate'],
                'dst_host_srv_diff_host_rate': form.cleaned_data['dst_host_srv_diff_host_rate'],
                'dst_host_serror_rate': form.cleaned_data['dst_host_serror_rate'],
                'dst_host_srv_serror_rate': form.cleaned_data['dst_host_srv_serror_rate'],
                'dst_host_rerror_rate': form.cleaned_data['dst_host_rerror_rate'],
                'dst_host_srv_rerror_rate': form.cleaned_data['dst_host_srv_rerror_rate'],
                'last_flag': form.cleaned_data['last_flag'],
            }
            prediction_result = predict_ml(data)
            return redirect('success')
        else:
            return HttpResponseBadRequest('Invalid form data')
    else:
        form = MyModelForm()
        return render(request, 'myapp/form.html', {'form': form})

