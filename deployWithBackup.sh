#!/bin/sh

#restart single and unique process
pythonFileName="server-register.py"
logFileName="log.out"
psid=0

checkpid() {
  echo "checkpid $1"
  psid=0
  aaps=`ps -ef | grep $1 | grep -v grep`
  
  
  if [ -n "$aaps" ]; then
  psid=`echo $aaps | awk '{print $2}'`
  else
  psid=0
  fi
  
  echo "checkpided: $psid"
}

dt=`date +%Y%m%d-%H%M%S`;
destFolder=backup/$dt/;
mkdir -p $destFolder;
tar cvfz $destFolder/bin.tar.gz bin/;
mv swap/* bin/ -f

checkpid $pythonFileName
echo "kill $psid ..."
if [ $psid -ne 0 ];then
  kill $psid
fi
sleep 1s
mv logs/$logFileName logs/$logFileName.$dt
cd bin
touch ../logs/$logFileName
#nohup python $pythonFileName > ../logs/$logFileName 1>../logs/$logFileName 2>../logs/$logFileName &
nohup python $pythonFileName & > ../logs/$logFileName
checkpid $pythonFileName
echo "new pid: $psid ..."
