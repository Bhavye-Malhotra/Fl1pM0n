# Fl1pM0n - Asset Monitoring tool

## **What is asset management?**

It’s basically a centralized way for you to monitor and manage your businesses' assets.

The great news is that, if done properly, you can increase productivity and efficiency within your department.

In our opinion, you’d be daft not to! Having such a tool in place will let you track the overall access of your assets. The data you get back will allow you to make sure assets are being utilized efficiently, and gives you the power to review performance and highlight additional unnecessary access.


## Proposed Approach

- Getting the Ip address of the device which accessed the asset.

- Scan the given Ip to collect comprehensive data.

- Storing that data in NoSQL database and making an API endpoint to fetch the contents of database.

- Maintaining a Web GUI which displays the results stored in the database and a functionality to segregate records on the basis of searches.


![image](https://user-images.githubusercontent.com/49281065/126897826-f70fc729-2538-482a-ba40-b9ef82b27f97.png)


## Limitations

- API Authentication is fragile

- Limited search functionality

- Scanning is not multi-threaded 

## Future Scope

- Adding a key signing authentication to access API

- Using Regex to increase search functionality

- Adding more information in scan like services running, ports opened, etc.

- Making Column filters in Web GUI.

- Integration for logging to a third party application like Slack/Discord/Telegram.




## Building
![Build](/BUILDME.png)

## Demo Video
[![Screenshot](https://img.youtube.com/vi/A3u3_C1lL-s/maxresdefault.jpg)](https://www.youtube.com/watch?v=A3u3_C1lL-s)

## Contributors ✨

Thanks goes to these wonderful people.

<table>
	<tr>
		<td>
			<a href="https://github.com/dscciem/Pentesting-and-Hacking-Scripts/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=dscciem/Pentesting-and-Hacking-Scripts" />
</a>
		</td>
	</tr>
</table>
