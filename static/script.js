const topics = ['Effect of the 2004 Indian Ocean earthquake on Norway', 'Alliance of European National Movements', 'Karl Dewey Myers', 'Powerade', 'Benjamin F. Randolph', 'Nasukarasuyama', 'Albuquerque, Texas', 'U.S. Route 212 in Minnesota', 'Jack Wilson Evans', 'Louis-Charles Le Vassor de La Touche', 'Al Palzer', 'John MacMillan (British Army officer)', 'Thoracic aorta', 'Cliff Hunt', 'Kiritappu Wetland', 'Chubba Purdy', 'Charlie Hunter', 'Rachel Harris', 'Daleks in Manhattan', 'Kempton Bunton', 'Jordanoleiopus inmbae', "2005 Women's British Open", 'Plaza Mayor de Lima', '30th Annual Grammy Awards', 'Raymond Desfossés', 'British Rail Class 05', 'Domo Genesis', 'WRBW', 'Kuala Berang Bridge', 'Vahid Bayatlou', 'Sack of Balbriggan', 'List of vassal prince peerages of the Ming dynasty', 'Katherine Lapp', 'Hidden Valley Resort', 'Garron', 'Travis Diener', 'Law & Order Organized Crime', 'A Burnt Child', 'Soil (American band)', 'Frederick William, Elector of Brandenburg', 'Gnaty-Lewiski', 'Randal MacDonnell, 1st Marquess of Antrim (1645 creation)', 'Honeymoon (Brooklyn Nine-Nine)', 'Daniel Altmaier', 'Sama Malolo', 'List of rivers of Hungary', 'Patrick Emerling', 'New York University Grossman School of Medicine', 'The Persistence of Memory (novel)', 'Lacropte', 'Everjets', 'Cannondale station', 'Siemens SX45', 'Tucuruí', 'The Voice of Midnight', 'Shai Ross', 'Charles Messier', 'Angelica archangelica', 'Purvesvara Siva Temple', 'Krosbi Mensah', 'Nelly (1798 ship)']
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