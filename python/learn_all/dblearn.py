#!/usr/bin/python
# -*- coding: UTF-8 -*-



url=raw_input("冒号后输入视频地址：")
urllist=list(url)

#www域名
if urllist[7:10]==['w','w','w']:
    urllist[7:10]=['m']
    url="".join(urllist)

#处理手游地址
if urllist[7:14]==['s', 'h', 'o', 'u', 'y', 'o', 'u']:
    urllist[7:14]=['m']
    url="".join(urllist)

content=urllib2.urlopen(url).read()               #获得网站源码
m=re.search(r'\bhttp\b.*\bmp4\b',content)         #在源码中寻找视频地址
a=m.group(0)                                      #调用方法获得符合条件的字符串
print a                                           #打印该视频地址


from urllib import urlopen
doc = urlopen("http://www.aipai.com").read()
print doc

conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="19900807",db="python_pc")
with conn:
    cursor = conn.cursor()
    cursor.execute ("insert into video_msg(id,video_url,mp4_url) values ('url+url','30018655','打酱油路过','1','2015-11-19')")
# cursor.execute(sql)
#row=cursor.fetchone()
#print row
cursor.close()
conn.close()




#!/usr/bin/python
# -*- coding: UTF-8 -*-

#定义变量
import random,MySQLdb,sys

#以下为变量赋值
zone_id = random.randint(1,10)*1111
v_id = random.randint(1,10)+1000
vv_number = random.uniform(0,1) * 300
sj_number = raw_input("输入使用虎牙源的几率：")
ydz_ap = "使用爱拍源"
ydz_hy = "使用虎牙源"
gg_hy = "使用虎牙广告"
gg_ap = "使用爱拍广告"
a=0

# 判断使用的视频源
def dy_ywj_dz(sj_number):
    if zone_id == [1111,2222,3333,4444]:
        print ydz_ap
    elif v_id == [1001,1002,1003,1004]:
        print ydz_ap
    elif vv_number > 150:
        print ydz_ap
    elif sj_number < random.uniform(0,1):
        print ydz_ap
    else:
        print ydz_hy
    return

dy_ywj_dz(sj_number)

if dy_ywj_dz(sj_number) == ydz_ap:
    print gg_ap
elif dy_ywj_dz(sj_number) == ydz_hy:
    print gg_hy













case 0:
	$message = "上传成功";
	break;
case 10001:
	$message = "参数不足";
	break;
# 是什么参数不足？

case 10002:
	$message = "参数类型不正确";
	break;	
# 什么参数类型不正确

case 10003:
	$message = "请求方式错误";
	break;
# 触发的方式是什么？

case 10004:
	$message = "请求接口不存在或未开放";
	break;
# 触发的方式是什么？理论上普通用户永远看不见吧

case 10005:
	$message = "请求太频繁";
	break;


case 10006:
	$message = "该平台未授权";
	break;

case 10010:
	$message = "用户未登录";
	break;

case 10011:
	$message = "用户未授权该平台";
	break;

case 10020:
	$message = "参数验证不通过";
	break;
# 什么参数验证不通过？能否实现返回具体的参数名称

case 10021:
	$message = "表单token验证不通过";
	break;
# 

case 10022:
	$message = "歌手数量不符合";
	break;
case 10023:
	$message = "曲风数量不符合";
	break;
case 10024:
	$message = "请选择语种";
	break;
case 10025:
	$message = "请选择曲风";
	break;
case 10026:
	$message = "音质不符合要求";
	break;
case 10027:
	$message = "请选择正确的歌曲版本";
	break;
case 10035:
	$message = "已授权的平台不可取消";
	break;
case 10101:
	$message = "上传文件为空";
	break;
case 10102:
	$message = "上传文件出错";
	break;
case 10103:
	$message = "上传文件不存在";
	break;
case 10104:
	$message = "文件大小不符合";
	break;
case 10105:
	$message = "文件类型不符合";
	break;
case 10106:
	$message = "分块数量超出总数";
	break;	
case 10107:
	$message = "保存音频分块失败";
	break;	
case 10108:
	$message = "文件分块合并失败";
	break;	
case 10109:
	$message = "获取音频信息失败";
	break;		
case 10110:
	$message = "上传文件失败";
	break;
case 10111:
	$message = "保存上传的文件信息失败";
	break;
case 10115:
	$message = "上传口令不存在";
	break;
case 10203:
	$message = "歌手必须包含当前音乐人";
	break;
case 10204:
	$message = "原创歌曲信息不存在";
	break;
case 10205:
	$message = "歌曲信息不存在";
	break;
case 10206:
	$message = "歌曲非用户所有";
	break;
case 10207:
	$message = "歌曲下载设置类型不允许";
	break;
case 10208:
	$message = "您已上传过该歌曲";
	break;
case 10209:
    $message = "存在敏感词";
    break;
case 10210:
	$message = "上传歌曲失败";
	break;
case 10230:
	$message = "修改歌曲失败";
	break;
case 10220:
	$message = "歌曲删除失败";
	break;
case 10311:
	$message = "专辑地区不符";
	break;
case 10312:
	$message = "专辑类别不符";
	break;
case 10313:
	$message = "专辑流派不符";
	break;
case 10314:
	$message = "专辑语言不符";
	break;
case 10320:
	$message = "专辑不存在";
	break;
case 10321:
	$message = "专辑不属于该用户";
	break;
case 10322:
	$message = "目标专辑不存在";
	break;


case 10323:
	$message = "目标专辑不属于该用户";
	break;
# 什么情况会触发

case 10324:
	$message = "用户没有默认专辑";
	break;
case 10325:
	$message = "默认专辑不可删除";
	break;

case 10326:
	$message = "选择歌曲不属于该专辑";
	break;
# 什么情况下回触发

case 10327:
	$message = "用户已存在默认专辑";
	break;
case 10328:
	$message = "创建默认专辑失败";
	break;
case 10329:
	$message = "原属专辑和目标专辑相同";
	break;
case 10331:
	$message = "添加专辑失败";
	break;
case 10332:
	$message = "编辑专辑保存失败";
	break;
case 10335:
	$message = "歌曲添加到专辑失败";
	break;
case 10400:
	$message = "时间区间设置不正确";
	break;
case 10401:
	$message = "收入类型不存在";
	break;
# 暂无这个反馈方式
case 10501:
	$message = "用户不存在";
	break;

case 10505:
	$message = "验证码不匹配";
	break;
case 10506:
	$message = "修改密码失败";
	break;
default:
	$message = "未知错误";
	break;









