echo "BUILD START"
python3.9 -mpip install -r requirements.txt
python3.9 manage.py collectstatic --no-input --clear
echo "BUILD END"