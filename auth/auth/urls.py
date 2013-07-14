from django.conf.urls.defaults import *
from loginsection.views import login_user,register_user,checkaround,checkedin,forget_password,selectinterest,profile
from django.contrib.auth.views import password_reset,PasswordResetForm,default_token_generator,SetPasswordForm,password_reset_confirm,password_reset_done

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^login/$', login_user),
	(r'^register/$',register_user),
	(r'^forgetpassword/$', 'django.contrib.auth.views.password_reset',{'template_name':'registration/password_reset_form.html','subject_template_name':'registration/password_reset_subject.txt','email_template_name':'registration/password_reset_email.html','password_reset_form':PasswordResetForm,'token_generator':default_token_generator}),
	(r'^password_reset_confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',{'post_reset_redirect':'login'}),
	(r'^login/$', 'django.contrib.auth.views.password_reset_done',{'template_name':'auth.html'}),
	(r'^specialinerest/$',selectinterest),
	(r'^login/profile/$', profile),
	(r'^checkedin/$', checkedin),
	(r'^checkaround/$', checkaround),

)
