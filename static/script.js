topics =['Rachel Harris', 'Millicent Rogers Museum', "2005 Women's British Open", 'Siemens SX45', 'New York University Grossman School of Medicine', 'Daleks in Manhattan', 'Albuquerque, Texas', 'U.S. Route 212 in Minnesota', 'Cannondale station', 'Garron', 'British Rail Class 05', 'Kuala Berang Bridge', 'The Persistence of Memory (novel)', 'Kiritappu Wetland', 'Al Palzer', 'Todd Simpson', 'Frederick William, Elector of Brandenburg', 'Jordanoleiopus inmbae', 'Perfect Strangers (2016 film)', 'Louis-Charles Le Vassor de La Touche', 'Jack Wilson Evans', 'John MacMillan (British Army officer)', 'Cliff Hunt', 'Gary Mabbutt', 'Karl Dewey Myers', 'Powerade', "Galileo's Dream", 'St Martin Outwich', 'List of vassal prince peerages of the Ming dynasty', 'Nasukarasuyama', 'Pennsylvania Route 201', 'Law & Order Organized Crime', 'Cape Cornwall Mine', 'Honeymoon (Brooklyn Nine-Nine)', 'Alliance of European National Movements', 'Generation time', 'Provisional Government of Missouri', 'Soil (American band)', 'Nelly (1798 ship)', 'Domo Genesis', 'Benjamin F. Randolph', 'Asthenozoospermia', '1853 McElroy', 'Charlie Hunter', 'Kempton Bunton', 'Hybrid system', 'List of awards and nominations received by Ajith Kumar', 'Travis Diener', 'Chadi Massaad', 'Everjets', 'Purvesvara Siva Temple', 'Chubba Purdy', 'Overseas trained doctors in Australia', 'Krosbi Mensah', 'Randal MacDonnell, 1st Marquess of Antrim (1645 creation)', 'A Burnt Child', 'Oedipus the King (1968 film)', 'The Voice of Midnight', 'Lacropte', 'Roman Catholic Diocese of Pueblo', 'Tucuruí', 'Thoracic aorta', 'Hidden Valley Resort', 'X the Unknown', 'Vahid Bayatlou', 'Angelica archangelica', 'Md. Khasruzzaman', '30th Annual Grammy Awards', 'Telespazio VEGA Deutschland', 'Effect of the 2004 Indian Ocean earthquake on Norway', 'WRBW', 'Plaza Mayor de Lima', 'List of rivers of Hungary', 'Gnaty-Lewiski', "2010 Women's Youth World Handball Championship", 'Raymond Desfossés', 'Charles Messier', 'Katherine Lapp', '2020–21 PGA Tour priority ranking', 'Almira Hershey', 'Daniel Altmaier', 'Patrick Emerling', 'Sack of Balbriggan', 'Korşirmat', 'Sama Malolo', "Hungarian Writers' Union", 'Shai Ross', 'Ernst Graf zu Reventlow']






const topicElement = document.getElementById('topic');

function getRandomTopic() {
  return topics[Math.floor(Math.random() * topics.length)];
}

function fadeIn(element) {
  element.style.opacity = 0;
  let opacity = 0;
  const intervalId = setInterval(() => {
    if (opacity >= 1) {
      clearInterval(intervalId);
    }
    element.style.opacity = opacity;
    opacity += 0.1;
  }, 50);
}

function fadeOut(element) {
  let opacity = 1;
  const intervalId = setInterval(() => {
    if (opacity <= 0) {
      clearInterval(intervalId);
    }
    element.style.opacity = opacity;
    opacity -= 0.1;
  }, 50);
}

function cycleTopics() {
  fadeOut(topicElement);
  setTimeout(() => {
    const randomTopic = getRandomTopic();
    topicElement.textContent = randomTopic;
    fadeIn(topicElement);
  }, 500);
}

setInterval(cycleTopics, 3000);