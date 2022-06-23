import unittest

from logic import check_posted_data

class TestSnippet(unittest.TestCase):
    
    def test_check_posted_data_first(self):
        print(f"Testing function - {check_posted_data.__name__}")
        
        data_list = [[{"x": 184,"y": 323},"add",200], [{"x": 143,"y": 0},"division",302]
                     , [{"x": 143},"division",301]]
        
        for data in data_list:
            
            result = check_posted_data(data[0],data[1])
            
            self.assertEqual(result, data[2])


    def test_check_posted_data_second(self):
        
        data_list = [[{"x": 184, "y": 323}, "add", 200], [
            {"x": 143, "y": 0}, "division", 302], [{"x": 143}, "division", 301]]

        for data in data_list:

            result = check_posted_data(data[0], data[1])

            self.assertEqual(result, data[2])
            
            print(f"Test data {data}")


if __name__ == "__main__":
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test_reports'))
    
rpm -Uvh https://repo.zabbix.com/zabbix/5.4/rhel/7/x86_64/zabbix-release-5.4-1.el7.noarch.rpm && yum install zabbix-agent -y
sed -i -e 's/\(Hostname=Zabbix server\).*//' /etc/zabbix/zabbix_agentd.conf && sed -i -e 's/\(Server=127.0.0.1\).*//' /etc/zabbix/zabbix_agentd.conf
echo Hostname=$(hostname -I | cut -f1 -d' ') >>/etc/zabbix/zabbix_agentd.conf && echo ServerActive=10.9.3.157 >>/etc/zabbix/zabbix_agentd.conf
echo StartAgents=0 >>/etc/zabbix/zabbix_agentd.conf
service zabbix-agent restart && systemctl enable zabbix-agent
firewall-cmd --zone=public --add-port=10050-10051/tcp --permanent
firewall-cmd --zone=public --add-port=11211-11221/tcp --permanent
firewall-cmd --reload
