import requests

try:
    response = requests.get("http://127.0.0.1:5000/get-logs")
    print(f"✅ Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Retrieved {len(data)} logs")
        
        if data:
            print("\n📊 Sample log:")
            print(f"   User: {data[0]['user_id']}")
            print(f"   Risk Score: {data[0]['risk_score']}")
            print(f"   Status: {data[0]['status']}")
    else:
        print(f"❌ Error: {response.text}")
        
except requests.exceptions.ConnectionError:
    print("❌ Cannot connect to backend. Make sure Flask is running on port 5000")
except Exception as e:
    print(f"❌ Error: {e}")
