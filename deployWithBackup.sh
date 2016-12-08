#!/bin/sh

#restart single and unique process
pythonFileName="server-register.py"
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
#kill $psid
sleep 1s
mv logs/nohup.out logs/nohup.out.$dt
cd bin
#nohup python $pythonFileName > ../logs/nohup.out &
checkpid $pythonFileName
echo "new pid: $psid ..."
