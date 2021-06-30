/* collecting template variables */

var title = JSON.parse(document.getElementById('title').textContent);
var subject_code = JSON.parse(document.getElementById('subject').textContent);
var get_subject_display = JSON.parse(document.getElementById('get_subject_display').textContent);
var content = JSON.parse(document.getElementById('content').textContent);
var channel = JSON.parse(document.getElementById('channel').textContent);
var important = JSON.parse(document.getElementById('important').textContent);

function log(msg) {
  var element = document.getElementById('console');
  element.insertAdjacentHTML('beforeend', '<br>' + '<samp>[pipeline.js] ' + msg + '</samp>');
}

log('WARNING: You are using a TYSK computer system. Abuse of this computer system, including abuse of the webhook system, will incur punishment. The script executes client-side but contains proprietary information, including all data held in the SQLite3 database.');

function getRoleID() {
  subject
  return subject_id
}

function discord() { /* https://dev.to/oskarcodes/send-automated-discord-messages-through-webhooks-using-javascript-1p01 */
  /* Channel */
  
  log('discord(): channel ' + channel)

  switch(channel) {
    case "MAIN":
      var channel_link = DISCORD_WEBHOOK_MAIN;
    case "LOWP":
      var channel_link = DISCORD_WEBHOOK_LOWP;
    case "META":
      var channel_link = DISCORD_WEBHOOK_META;
  }
  
  /* Title */

  var subject_id = SUBJECT_ROLE_IDS[subject_code];

  var discord_title = "undefined";

  if (subject == "Other" || subject == "Meta") {
    log('discord(): subject == "Other"')
     var discord_title = '**' + title + '**';
  }

  if (subject != "Other" || subject != "Meta") {
    log('discord(): subject != "Other"')
    var discord_title = '**<@&' + subject_id + '>**';
  }

  /* Important ping */

  var discord_content = discord_title + '\n\n' + content;

  if (important == true) {
    log('discord(): important == true')
    important_content = "\n\n> @everyone";
    discord_content += important_content;
    log('discord(): discord_content +=: ' + discord_content);
  }

  /* Attachments */

  /* POST */

  var request = new XMLHttpRequest();
  request.open("POST", channel_link);
  log('discord(): XMLHTTPRequest opened')

  request.setRequestHeader('Content-type', 'application/json');

  var params = {
    username: "Things You Should Know",
    avatar_url: "https://cdn.discordapp.com/attachments/697947241490677820/859034270739595274/TYSK.jpg",
    content: discord_content
  }

  request.send(JSON.stringify(params));

  log('discord(): Discord webhook sent')
}

async function pipeline() {
  log('Start');
}

log('Turned on!');

pipeline();
discord();

log('Script end.')
