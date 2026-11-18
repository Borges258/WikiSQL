# Error cases

## test:5:1-10083598-1

- Question: What was the number of race that Kevin Curtain won?
- Gold: `{"sel": 0, "conds": [[4, 0, "Kevin Curtain"]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[6, 0, "Kevin Curtain"]], "sel": 0}`
- Error: logical-form mismatch

## test:19:1-1015521-2

- Question: Give me a list of all spanish officer titles that could receive recognition as group captain in english
- Gold: `{"sel": 2, "conds": [[3, 0, "Group Captain"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Group Captain"]], "sel": 1}`
- Error: logical-form mismatch

## test:35:1-10333757-1

- Question: What is the Frequency at the Market/Rank of Burlington - Plattsburgh , Vermont - New York /143?
- Gold: `{"sel": 1, "conds": [[4, 0, "Burlington - Plattsburgh , Vermont - New York /143"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "Burlington - Plattsburgh , Vermont - New York /143"]], "sel": 1}`
- Error: logical-form mismatch

## test:90:1-10718868-2

- Question: How many episodes in season 6 titles "Poppin' Tags"?
- Gold: `{"sel": 1, "conds": [[2, 0, "\"Poppin' Tags\""]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[1, 0, 6], [2, 0, "\"Poppin' Tags\""]], "sel": 0}`
- Error: logical-form mismatch

## test:124:1-11075747-3

- Question: How many series are named "Lockdown"?
- Gold: `{"sel": 0, "conds": [[2, 0, "\"Lockdown\""]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "Lockdown"]], "sel": 0}`
- Error: logical-form mismatch

## test:126:1-11075747-3

- Question: What was the latest episode of "House of Cards"?
- Gold: `{"sel": 1, "conds": [[2, 0, "\"House of Cards\""]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[2, 0, "House of Cards"]], "sel": 1}`
- Error: logical-form mismatch

## test:131:1-1108394-6

- Question: What was the total number in Manhattan when Staten Island was 12,658?
- Gold: `{"sel": 1, "conds": [[5, 0, "12,658"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "12,658"]], "sel": 1}`
- Error: logical-form mismatch

## test:143:1-11157122-5

- Question: What was Eric Dickerson's longest run?
- Gold: `{"sel": 5, "conds": [[0, 0, "Eric Dickerson"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Eric Dickerson"]], "sel": 5}`
- Error: logical-form mismatch

## test:146:1-11206916-1

- Question: What was the highest amount of people that attended the elgin city team?
- Gold: `{"sel": 3, "conds": [[0, 0, "Elgin City"]], "agg": 3}`
- Prediction: `{"agg": 1, "conds": [[0, 0, "Elgin City"]], "sel": 3}`
- Error: logical-form mismatch

## test:160:1-11233358-2

- Question: During the 2013 debut, what is the w-I(total) number?
- Gold: `{"sel": 1, "conds": [[5, 0, 2013]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, 2013]], "sel": 1}`
- Error: logical-form mismatch

## test:177:1-1133844-4

- Question: who were the winners in west virginia
- Gold: `{"sel": 5, "conds": [[0, 0, "West Virginia"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "West Virginia"]], "sel": 1}`
- Error: logical-form mismatch

## test:178:1-1133844-4

- Question: tell the final for lindsey graham
- Gold: `{"sel": 4, "conds": [[1, 0, "Lindsey Graham"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Lindsey Graham"]], "sel": 5}`
- Error: logical-form mismatch

## test:179:1-1133844-4

- Question: who won the senate seat in arkansas
- Gold: `{"sel": 1, "conds": [[0, 0, "Arkansas"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Arkansas"]], "sel": 5}`
- Error: logical-form mismatch

## test:234:1-1145977-2

- Question: When did the season air where the viewership was 14.71 million?
- Gold: `{"sel": 1, "conds": [[5, 0, "14.71"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "14.71"]], "sel": 3}`
- Error: logical-form mismatch

## test:243:1-11497980-1

- Question: If the engine make/capacity is MWM 6.10 TCA-EURO III (Turbo Intercooler) and  GVM (kg) Technical Capacity is 23000, what is the Torque Nm@rpm?
- Gold: `{"sel": 3, "conds": [[6, 0, "23000"], [1, 0, "MWM 6.10 TCA-EURO III (Turbo Intercooler)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "MWM 6.10 TCA-EURO III (Turbo Intercooler)"], [5, 0, "23000"]], "sel": 3}`
- Error: logical-form mismatch

## test:244:1-11497980-1

- Question: What is the power kw@RPM of the 13.180 model?
- Gold: `{"sel": 2, "conds": [[0, 0, "13.180"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "13.180"]], "sel": 2}`
- Error: logical-form mismatch

## test:266:1-11622392-1

- Question: What is the sum of the largest purse?
- Gold: `{"sel": 3, "conds": [], "agg": 1}`
- Prediction: `{"agg": 4, "conds": [], "sel": 3}`
- Error: logical-form mismatch

## test:272:1-11630008-4

- Question: What is the series number for the title "Bad Influence"
- Gold: `{"sel": 0, "conds": [[2, 0, "\"Bad Influence\""]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Bad Influence"]], "sel": 0}`
- Error: logical-form mismatch

## test:312:1-11677691-7

- Question: Which player is from Saguaro High School?
- Gold: `{"sel": 1, "conds": [[2, 0, "Saguaro High School"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Saguaro High School"]], "sel": 0}`
- Error: logical-form mismatch

## test:320:1-11690135-1

- Question: Who had an evening gown score of 9.78?
- Gold: `{"sel": 1, "conds": [[3, 0, "9.78"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "9.78"]], "sel": 0}`
- Error: logical-form mismatch

## test:321:1-11690135-1

- Question: How many interviews were there for Miss Virginia?
- Gold: `{"sel": 1, "conds": [[0, 0, "Virginia"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Virginia"]], "sel": 1}`
- Error: logical-form mismatch

## test:322:1-11690135-1

- Question: Who had a swimsuit score of 9.87?
- Gold: `{"sel": 0, "conds": [[2, 0, "9.87"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "9.87"]], "sel": 0}`
- Error: logical-form mismatch

## test:325:1-11690135-1

- Question: Who scored a 9.72 in the swimsuit?
- Gold: `{"sel": 1, "conds": [[2, 0, "9.72"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "9.72"]], "sel": 0}`
- Error: logical-form mismatch

## test:327:1-11695215-1

- Question: How many episodes did David Jackson write and direct?
- Gold: `{"sel": 4, "conds": [[3, 0, "David Jackson"]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "David Jackson"], [4, 0, "David Jackson"]], "sel": 0}`
- Error: logical-form mismatch

## test:354:1-11827596-2

- Question: who is the music director for the song "jekhanete jaai ami 1"?
- Gold: `{"sel": 4, "conds": [[1, 0, "\"Jekhanete Jaai Ami 1\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "jekhanete jaai ami 1"]], "sel": 4}`
- Error: logical-form mismatch

## test:363:1-11869952-1

- Question: Which authority has a rocket launch called rehbar-5?
- Gold: `{"sel": 6, "conds": [[0, 0, "Rehbar-5"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "rehbar-5"]], "sel": 3}`
- Error: logical-form mismatch

## test:385:1-11944282-1

- Question: What is the total amount of allied-unrelated where the component is human capital?
- Gold: `{"sel": 3, "conds": [[0, 0, "Human Capital"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "human capital"]], "sel": 3}`
- Error: logical-form mismatch

## test:386:1-11944282-1

- Question: How many integrated allied-related are there?
- Gold: `{"sel": 1, "conds": [[2, 0, "Many"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [], "sel": 2}`
- Error: logical-form mismatch

## test:388:1-11944282-1

- Question: what is the integrated in which the holding allied-unrelated is many?
- Gold: `{"sel": 4, "conds": [[3, 0, "Many"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "many"]], "sel": 1}`
- Error: logical-form mismatch

## test:389:1-11944282-1

- Question: What is the name of the integrated where allied-related is shared?
- Gold: `{"sel": 0, "conds": [[2, 0, "Shared"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "shared"]], "sel": 1}`
- Error: logical-form mismatch

## test:398:1-11964154-2

- Question: How many games was Damien Wilkins (27) the high scorer?
- Gold: `{"sel": 0, "conds": [[4, 0, "Damien Wilkins (27)"]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "Damien Wilkins (27)"]], "sel": 0}`
- Error: logical-form mismatch

## test:405:1-12032893-1

- Question: What number (#) is associated with the Name Ron Baxter?
- Gold: `{"sel": 1, "conds": [[0, 0, "Ron Baxter"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Ron Baxter"]], "sel": 1}`
- Error: logical-form mismatch

## test:424:1-12077540-1

- Question: There are 5 imports of plywood.
- Gold: `{"sel": 4, "conds": [[1, 0, "Plywood"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "5"], [1, 0, "plywood"]], "sel": 0}`
- Error: logical-form mismatch

## test:430:1-12094300-1

- Question: What is the average score when the swimsuit score is 8.503?
- Gold: `{"sel": 5, "conds": [[3, 0, "8.503"]], "agg": 0}`
- Prediction: `{"agg": 5, "conds": [[3, 0, "8.503"]], "sel": 5}`
- Error: logical-form mismatch

## test:438:1-12165135-1

- Question: What is the pick number of the defensive back?
- Gold: `{"sel": 0, "conds": [[3, 0, "Defensive Back"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Defensive Back"]], "sel": 0}`
- Error: logical-form mismatch

## test:452:1-12175755-1

- Question: What theme placed as #3 in the finale?
- Gold: `{"sel": 5, "conds": [[1, 0, "Finale"], [4, 0, "3"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Finale"], [4, 0, "3"]], "sel": 1}`
- Error: logical-form mismatch

## test:456:1-12175755-1

- Question: What is the song choice when the theme is not aired?
- Gold: `{"sel": 1, "conds": [[2, 0, "Not Aired"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "not aired"]], "sel": 2}`
- Error: logical-form mismatch

## test:457:1-12194021-1

- Question: What years did Markose Bristow Madhumita Bisht win the mens singles and/or the mixed doubles?
- Gold: `{"sel": 1, "conds": [[5, 0, "Markose Bristow Madhumita Bisht"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "Markose Bristow Madhumita Bisht"]], "sel": 0}`
- Error: logical-form mismatch

## test:460:1-12194021-1

- Question: In womens doubles and mens singles, what years did Arvind Bhat or Valiyaveetil Diju Jwala Gutta win?
- Gold: `{"sel": 4, "conds": [[1, 0, "Arvind Bhat"], [5, 0, "Valiyaveetil Diju Jwala Gutta"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Arvind Bhat"], [5, 0, "Valiyaveetil Diju Jwala Gutta"]], "sel": 0}`
- Error: logical-form mismatch

## test:461:1-12194021-1

- Question: How many titles did Trupti Murgunde claim?
- Gold: `{"sel": 4, "conds": [[2, 0, "Trupti Murgunde"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "Trupti Murgunde"]], "sel": 2}`
- Error: logical-form mismatch

## test:469:1-12226390-7

- Question: How many episodes had a title "the great mayoralty campaign"?
- Gold: `{"sel": 3, "conds": [[2, 0, "\"The Great Mayoralty Campaign\""]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "the great mayoralty campaign"]], "sel": 2}`
- Error: logical-form mismatch

## test:477:1-12261926-2

- Question: What is the general classification with the winner being evgeni berzin?
- Gold: `{"sel": 2, "conds": [[1, 0, "Evgeni Berzin"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Evgeni Berzin"]], "sel": 2}`
- Error: logical-form mismatch

## test:495:1-1231316-4

- Question: Where is Dwain Chambers from
- Gold: `{"sel": 6, "conds": [[3, 0, "Dwain Chambers"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Dwain Chambers"]], "sel": 4}`
- Error: logical-form mismatch

## test:496:1-1231316-4

- Question: What was the stats of Trinidad and Tobago
- Gold: `{"sel": 2, "conds": [[4, 0, "Trinidad and Tobago"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "Trinidad and Tobago"]], "sel": 1}`
- Error: logical-form mismatch

## test:506:1-12434380-1

- Question: When was the institution of Kansas city Kansas community college founded?
- Gold: `{"sel": 2, "conds": [[0, 0, "Kansas City Kansas Community College"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Kansas city Kansas community college"]], "sel": 2}`
- Error: logical-form mismatch

## test:517:1-12451376-2

- Question: What is the production code of the episode titled, "But there's Clay"?
- Gold: `{"sel": 6, "conds": [[2, 0, "\"But There's Clay\""]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "But There's Clay"]], "sel": 6}`
- Error: logical-form mismatch

## test:520:1-12451376-2

- Question: What is the number of the original airdate with the production code 208.
- Gold: `{"sel": 5, "conds": [[6, 0, 208]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[6, 0, 208]], "sel": 5}`
- Error: logical-form mismatch

## test:522:1-1251878-3

- Question: What is the size when the frame is bigger than for 4096.0
- Gold: `{"sel": 4, "conds": [[1, 1, 4096.0]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 1, 4096.0]], "sel": 0}`
- Error: logical-form mismatch

## test:523:1-1251878-3

- Question: What is the smallest frames per minute when the pixels are 5.0
- Gold: `{"sel": 7, "conds": [[3, 0, "5.0"]], "agg": 0}`
- Prediction: `{"agg": 2, "conds": [[3, 0, "5.0"]], "sel": 5}`
- Error: logical-form mismatch

## test:565:1-12828723-4

- Question: what is the points for when the played is 22 and tries against is 68?
- Gold: `{"sel": 5, "conds": [[1, 0, "22"], [8, 0, "68"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "22"], [8, 0, "68"]], "sel": 11}`
- Error: logical-form mismatch

## test:574:1-12828723-5

- Question: What was the lost with tries for?
- Gold: `{"sel": 4, "conds": [[7, 0, "Tries for"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [], "sel": 4}`
- Error: logical-form mismatch

## test:596:1-12962773-12

- Question: What is the height for player number 5?
- Gold: `{"sel": 2, "conds": [[0, 0, 5]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 5]], "sel": 2}`
- Error: logical-form mismatch

## test:598:1-12962773-12

- Question: WHat is the number for the player whose height is 2.01?
- Gold: `{"sel": 1, "conds": [[2, 0, "2.01"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "2.01"]], "sel": 0}`
- Error: logical-form mismatch

## test:599:1-12962773-12

- Question: What year was the player with the height 2.04 born?
- Gold: `{"sel": 4, "conds": [[2, 0, "2.04"]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "2.04"]], "sel": 4}`
- Error: logical-form mismatch

## test:616:1-1300525-1

- Question: What is the capital of the district who's simplified name is  信州区?
- Gold: `{"sel": 3, "conds": [[1, 0, "信州区"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "信州区"]], "sel": 0}`
- Error: logical-form mismatch

## test:618:1-1300525-1

- Question: What is the density of yushan county?
- Gold: `{"sel": 6, "conds": [[0, 0, "Yushan County"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Yushan County"]], "sel": 6}`
- Error: logical-form mismatch

## test:621:1-13050822-2

- Question: What is the time for stage ss18?
- Gold: `{"sel": 6, "conds": [[1, 0, "SS18"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "ss18"]], "sel": 2}`
- Error: logical-form mismatch

## test:623:1-13050822-2

- Question: What is the number of leg for ss17
- Gold: `{"sel": 0, "conds": [[1, 0, "SS17"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "ss17"]], "sel": 0}`
- Error: logical-form mismatch

## test:641:1-13241993-3

- Question: When did the part 1 of the episode "Anxiety" air?
- Gold: `{"sel": 2, "conds": [[1, 0, "\"Anxiety\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Anxiety"]], "sel": 2}`
- Error: logical-form mismatch

## test:644:1-13241993-3

- Question: What's the episode number of "Anxiety"?
- Gold: `{"sel": 0, "conds": [[1, 0, "\"Anxiety\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Anxiety"]], "sel": 0}`
- Error: logical-form mismatch

## test:660:1-13336122-7

- Question: When did the episode "Hell bent for leather" originally air?
- Gold: `{"sel": 5, "conds": [[2, 0, "\"Hell Bent for Leather\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Hell bent for leather"]], "sel": 5}`
- Error: logical-form mismatch

## test:711:1-1341568-48

- Question: What was the result of the election in the district whose incumbent is Tom Foley?
- Gold: `{"sel": 4, "conds": [[1, 0, "Tom Foley"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Tom Foley"]], "sel": 5}`
- Error: logical-form mismatch

## test:770:1-1342249-42

- Question: How many results have Jere Cooper as incumbent?
- Gold: `{"sel": 4, "conds": [[1, 0, "Jere Cooper"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "Jere Cooper"]], "sel": 4}`
- Error: logical-form mismatch

## test:771:1-1342256-13

- Question: Who won the election of 1942 in the district Illinois 13?
- Gold: `{"sel": 1, "conds": [[0, 0, "Illinois 13"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Illinois 13"]], "sel": 5}`
- Error: logical-form mismatch

## test:780:1-1342379-5

- Question: Who was the incumbent when henry e. barbour ran?
- Gold: `{"sel": 5, "conds": [[1, 0, "Henry E. Barbour"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "Henry E. Barbour"]], "sel": 1}`
- Error: logical-form mismatch

## test:789:1-1342393-42

- Question: What was the total number of votes for Tom Connally
- Gold: `{"sel": 3, "conds": [[1, 0, "Tom Connally"]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "Tom Connally"]], "sel": 5}`
- Error: logical-form mismatch

## test:807:1-13464416-6

- Question: how many times was the participation at omni coliseum 7,194?
- Gold: `{"sel": 0, "conds": [[7, 0, "Omni Coliseum 7,194"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[7, 0, "Omni Coliseum 7,194"]], "sel": 8}`
- Error: logical-form mismatch

## test:808:1-1354805-3

- Question: The minimum average number of dancers is 34.1 how many times
- Gold: `{"sel": 4, "conds": [[5, 0, "34.1"]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[5, 0, "34.1"]], "sel": 4}`
- Error: logical-form mismatch

## test:809:1-1354805-3

- Question: What is the Number of dances is 11 and competition finish is larger than 2.0 total
- Gold: `{"sel": 3, "conds": [[4, 0, 11], [1, 1, 2.0]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 0, 11], [1, 1, 2.0]], "sel": 4}`
- Error: logical-form mismatch

## test:821:1-1359212-2

- Question: where is hte second place winner from united kingdom?
- Gold: `{"sel": 1, "conds": [[7, 0, "United Kingdom"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[7, 0, "United Kingdom"]], "sel": 10}`
- Error: logical-form mismatch

## test:824:1-1359212-2

- Question: what amount has spain as second place and the language is russian?
- Gold: `{"sel": 6, "conds": [[7, 0, "Spain"], [2, 0, "Russian"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[7, 0, "Spain"], [2, 0, "Russian"]], "sel": 5}`
- Error: logical-form mismatch

## test:825:1-13605170-2

- Question: how many Curtiss XBTC aircraft are retired?
- Gold: `{"sel": 4, "conds": [[0, 0, "Curtiss XBTC"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "curtiss xbtc"]], "sel": 4}`
- Error: logical-form mismatch

## test:856:1-13643154-2

- Question: What is the most rnd for watkins glen?
- Gold: `{"sel": 0, "conds": [[1, 0, "Watkins Glen"]], "agg": 2}`
- Prediction: `{"agg": 1, "conds": [[1, 0, "Watkins Glen"]], "sel": 0}`
- Error: logical-form mismatch

## test:869:1-13758243-1

- Question: What numer pick in the draft for jerry hill?
- Gold: `{"sel": 4, "conds": [[1, 0, "Jerry Hill"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "jerry hill"]], "sel": 4}`
- Error: logical-form mismatch

## test:896:1-13870048-3

- Question: what was the lowest numbers for the winner gregory w. meeks
- Gold: `{"sel": 3, "conds": [[1, 0, "Gregory W. Meeks"]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[1, 0, "Gregory W. Meeks"]], "sel": 0}`
- Error: logical-form mismatch

## test:902:1-1389609-3

- Question: What is the highest number where the portion of observers is 0.163%?
- Gold: `{"sel": 2, "conds": [[3, 0, "0.163%"]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[3, 0, "0.163%"]], "sel": 1}`
- Error: logical-form mismatch

## test:908:1-14035132-3

- Question: On what date did the episode with a series number 31, with a story written by William Reiss, air for the first time? 
- Gold: `{"sel": 6, "conds": [[5, 0, "William Reiss"], [0, 0, "31"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "31"], [4, 3, "William Reiss"]], "sel": 6}`
- Error: operator 3 is not executable

## test:914:1-1404486-1

- Question: what is the number of area where the county is marsabit?
- Gold: `{"sel": 3, "conds": [[1, 0, "Marsabit"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Marsabit"]], "sel": 3}`
- Error: logical-form mismatch

## test:916:1-14070062-3

- Question: What's the tries against count of the team with 396 points against? 
- Gold: `{"sel": 8, "conds": [[6, 0, "396"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "396"]], "sel": 8}`
- Error: logical-form mismatch

## test:918:1-14070062-3

- Question: What's the tries for count for the team with 70 points? 
- Gold: `{"sel": 7, "conds": [[11, 0, "70"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[11, 0, "70"]], "sel": 7}`
- Error: logical-form mismatch

## test:920:1-14070062-3

- Question: What's the losing bonus count for the club with 9 won games? 
- Gold: `{"sel": 10, "conds": [[2, 0, "9"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "9"]], "sel": 10}`
- Error: logical-form mismatch

## test:922:1-1409106-2

- Question: How many home wins occured win the road games are larger than 3.0 but road win percentage is .000?
- Gold: `{"sel": 10, "conds": [[16, 0, ".000"], [13, 1, 3.0]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[13, 1, 3.0], [16, 0, ".000"]], "sel": 10}`
- Error: logical-form mismatch

## test:926:1-140968-1

- Question: How many copoes per particle are created in the segment that forms inner shell of the core?
- Gold: `{"sel": 5, "conds": [[4, 0, "Forms inner shell of the core"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "Forms inner shell of the core"]], "sel": 5}`
- Error: logical-form mismatch

## test:928:1-140968-1

- Question: How many base pairs are there if the molecular weight is 102?
- Gold: `{"sel": 1, "conds": [[3, 0, "102"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "102"]], "sel": 1}`
- Error: logical-form mismatch

## test:929:1-140968-1

- Question: How many copies per particle are there for the base pair that is size 1059?
- Gold: `{"sel": 5, "conds": [[1, 0, 1059]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, 1059]], "sel": 5}`
- Error: logical-form mismatch

## test:957:1-1420954-1

- Question: elaine lee worked on how many issues
- Gold: `{"sel": 1, "conds": [[2, 0, "Elaine Lee"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Elaine Lee"]], "sel": 1}`
- Error: logical-form mismatch

## test:963:1-14253123-1

- Question: When Spencer is the county  what is total of the population (2010) (rank)? 
- Gold: `{"sel": 5, "conds": [[1, 0, "Spencer"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "Spencer"]], "sel": 5}`
- Error: logical-form mismatch

## test:969:1-14242137-4

- Question: Name the oberliga for where tsv 1860 munich and borussia neunkirchen
- Gold: `{"sel": 3, "conds": [[1, 0, "TSV 1860 Munich"], [4, 0, "Borussia Neunkirchen"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "tsv 1860 munich"], [4, 0, "borussia neunkirchen"]], "sel": 0}`
- Error: logical-form mismatch

## test:973:1-14260687-3

- Question: During the quarter of 2012 Q2, how many millions of Blackberry OS phones where shipped when 0.1 million others were shipped?
- Gold: `{"sel": 4, "conds": [[7, 0, "0.1"], [0, 0, "2012 Q2"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "2012 Q2"], [7, 0, "0.1"]], "sel": 4}`
- Error: logical-form mismatch

## test:974:1-14260687-3

- Question: During the quarter 2012 Q4, how many millions of android phones were shipped?
- Gold: `{"sel": 1, "conds": [[0, 0, "2012 Q4"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "2012 Q4"]], "sel": 1}`
- Error: logical-form mismatch

## test:976:1-14260687-3

- Question: How many total smartphones were shipped during the quarter 2012 Q1?
- Gold: `{"sel": 8, "conds": [[0, 0, "2012 Q1"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "2012 Q1"]], "sel": 8}`
- Error: logical-form mismatch

## test:978:1-14260687-3

- Question: How man "other" millions of smartphones were shipped when 181.1 million total were shipped?
- Gold: `{"sel": 7, "conds": [[8, 0, "181.1"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[8, 0, "181.1"]], "sel": 7}`
- Error: logical-form mismatch

## test:1002:1-14330096-3

- Question: What number from the total number of episodes is the episode written by Julian Unthank?
- Gold: `{"sel": 1, "conds": [[3, 0, "Julian Unthank"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Julian Unthank"]], "sel": 0}`
- Error: logical-form mismatch

## test:1007:1-14342210-13

- Question: How many Games Started are there for Hugh White ?
- Gold: `{"sel": 2, "conds": [[0, 0, "Hugh White"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Hugh White"]], "sel": 2}`
- Error: logical-form mismatch

## test:1012:1-14342210-14

- Question: How many field goals did Walter Shaw make?
- Gold: `{"sel": 3, "conds": [[0, 0, "Walter Shaw"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Walter Shaw"]], "sel": 3}`
- Error: logical-form mismatch

## test:1014:1-14342210-14

- Question: How many touchdowns were made by the person with 7 extra points?
- Gold: `{"sel": 1, "conds": [[2, 0, 7]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, 7]], "sel": 1}`
- Error: logical-form mismatch

## test:1034:1-14342480-15

- Question: How many points did Duncan Thompson score?
- Gold: `{"sel": 4, "conds": [[0, 0, "Duncan Thompson"]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Duncan Thompson"]], "sel": 4}`
- Error: logical-form mismatch

## test:1040:1-14342592-5

- Question: When the total points are 22 how many total touchdowns have been made?
- Gold: `{"sel": 3, "conds": [[6, 0, 22]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[6, 0, 22]], "sel": 3}`
- Error: logical-form mismatch

## test:1043:1-14342480-7

- Question: How many points were scored by Rolla Bigelow?
- Gold: `{"sel": 6, "conds": [[0, 0, "Rolla Bigelow"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Rolla Bigelow"]], "sel": 6}`
- Error: logical-form mismatch

## test:1056:1-14389782-2

- Question: How many lost games for jersey number 2 and games started is less than 7.0?
- Gold: `{"sel": 4, "conds": [[1, 0, "2"], [2, 2, 7.0]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "2"], [2, 2, 7.0]], "sel": 4}`
- Error: logical-form mismatch

## test:1065:1-14407512-24

- Question: Name the number of overall nt points for 248.9
- Gold: `{"sel": 6, "conds": [[5, 0, "248.9"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "248.9"]], "sel": 6}`
- Error: logical-form mismatch

## test:1078:1-14598-5

- Question: How many buddhists are where s jain have 941?
- Gold: `{"sel": 5, "conds": [[6, 0, "941"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[6, 0, "941"]], "sel": 5}`
- Error: logical-form mismatch

## test:1081:1-14598-5

- Question: What is the data point for s hindu where the buddhist data point is 73.0%?
- Gold: `{"sel": 1, "conds": [[5, 0, "73.0%"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "73.0%"]], "sel": 1}`
- Error: logical-form mismatch

## test:1102:1-1473672-7

- Question: How many players had been drafted in front of Yves archambault
- Gold: `{"sel": 0, "conds": [[1, 0, "Yves Archambault"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 2, 110]], "sel": 1}`
- Error: logical-form mismatch

## test:1111:1-14752049-3

- Question: Name the international tourist arrivals for arrivals 2011 for 8.1 million
- Gold: `{"sel": 3, "conds": [[2, 0, "8.1 million"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "8.1 million"]], "sel": 1}`
- Error: logical-form mismatch

## test:1124:1-148386-2

- Question: How many roles include George Broderick in the casino 1888 theater?
- Gold: `{"sel": 0, "conds": [[2, 0, "George Broderick"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "George Broderick"]], "sel": 0}`
- Error: logical-form mismatch

## test:1130:1-14925084-1

- Question: Name the population 1891 for area being 175836
- Gold: `{"sel": 2, "conds": [[1, 0, 175836]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, 175836]], "sel": 2}`
- Error: logical-form mismatch

## test:1133:1-14925084-1

- Question: Name the number of administrative county for area 1961 and 176694
- Gold: `{"sel": 0, "conds": [[3, 0, 176694]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, 176694]], "sel": 0}`
- Error: logical-form mismatch

## test:1135:1-14940519-1

- Question: Name the number of week for game site being memorial stadium for buffalo bills
- Gold: `{"sel": 0, "conds": [[5, 0, "Memorial Stadium"], [2, 0, "Buffalo Bills"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "Memorial Stadium"], [2, 0, "Buffalo Bills"]], "sel": 0}`
- Error: logical-form mismatch

## test:1160:1-14977252-2

- Question: Name the jury of 10 points
- Gold: `{"sel": 5, "conds": [[4, 0, 10]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[6, 0, 10]], "sel": 1}`
- Error: logical-form mismatch

## test:1213:1-15261-1

- Question: What is the voltage range (v) if the clock multiplier is 3x or 2x mode and part number is a80486dx4wb-100?
- Gold: `{"sel": 3, "conds": [[5, 0, "3X or 2X mode"], [4, 0, "A80486DX4WB-100"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "3x or 2x mode"], [4, 0, "a80486dx4wb-100"]], "sel": 3}`
- Error: logical-form mismatch

## test:1216:1-15261-1

- Question: What is the processor speed (mhz) for part number a80486dx4-75?
- Gold: `{"sel": 0, "conds": [[4, 0, "A80486DX4-75"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "a80486dx4-75"]], "sel": 0}`
- Error: logical-form mismatch

## test:1227:1-15353123-1

- Question: Who was the highest pick
- Gold: `{"sel": 1, "conds": [], "agg": 2}`
- Prediction: `{"agg": 1, "conds": [], "sel": 1}`
- Error: logical-form mismatch

## test:1228:1-15353123-1

- Question: Who was the highest picked defensive end
- Gold: `{"sel": 1, "conds": [[3, 0, "Defensive end"]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "defensive end"]], "sel": 2}`
- Error: logical-form mismatch

## test:1236:1-15366768-1

- Question: What is the total number of N for the element with nuclide of 141 pr?
- Gold: `{"sel": 3, "conds": [[1, 0, "141 Pr"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "141 pr"]], "sel": 3}`
- Error: logical-form mismatch

## test:1249:1-15431251-1

- Question: What is the title for episode number 7 in the season?
- Gold: `{"sel": 2, "conds": [[0, 0, 7]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 7]], "sel": 2}`
- Error: logical-form mismatch

## test:1265:1-15467476-2

- Question: Name the points for  pontrhydyfen rfc
- Gold: `{"sel": 11, "conds": [[0, 0, "Pontrhydyfen RFC"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Pontrhydyfen RFC"]], "sel": 5}`
- Error: logical-form mismatch

## test:1267:1-15467476-2

- Question: Name the points for where lost is 4
- Gold: `{"sel": 5, "conds": [[4, 0, "4"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "4"]], "sel": 5}`
- Error: logical-form mismatch

## test:1294:1-15637071-1

- Question: How large is the fleet size of the airline with the IATA code of 5j?
- Gold: `{"sel": 5, "conds": [[2, 0, "5J"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "5j"]], "sel": 5}`
- Error: logical-form mismatch

## test:1299:1-15624586-2

- Question: Which country mines 24.0% of the world demand of uranium?
- Gold: `{"sel": 3, "conds": [[2, 0, "24.0%"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "24.0%"]], "sel": 0}`
- Error: logical-form mismatch

## test:1305:1-1566848-6

- Question: Name the number of pictorials for 5-85
- Gold: `{"sel": 5, "conds": [[0, 0, "5-85"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "5-85"]], "sel": 5}`
- Error: logical-form mismatch

## test:1314:1-1571238-2

- Question: When colgate is the team how many times did they place fourth?
- Gold: `{"sel": 4, "conds": [[0, 0, "Colgate"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Colgate"]], "sel": 4}`
- Error: logical-form mismatch

## test:1317:1-1571238-2

- Question: When the team is Toronto how many times did they place third?
- Gold: `{"sel": 3, "conds": [[0, 0, "Toronto"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Toronto"]], "sel": 3}`
- Error: logical-form mismatch

## test:1321:1-15739098-1

- Question: Name the msot episode that was adapted by leon griffiths
- Gold: `{"sel": 0, "conds": [[3, 0, "Leon Griffiths"]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Leon Griffiths"]], "sel": 1}`
- Error: logical-form mismatch

## test:1343:1-15824796-5

- Question: What is the airdate when the title is "topsy turvy"?
- Gold: `{"sel": 5, "conds": [[2, 0, "\"Topsy Turvy\""]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "topsy turvy"]], "sel": 5}`
- Error: logical-form mismatch

## test:1348:1-1585112-2

- Question: Name the road wins
- Gold: `{"sel": 14, "conds": [], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [], "sel": 14}`
- Error: logical-form mismatch

## test:1375:1-15928363-1

- Question: Name the number of horizontal when framerate hz is 25
- Gold: `{"sel": 1, "conds": [[5, 0, "25"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "25"]], "sel": 1}`
- Error: logical-form mismatch

## test:1378:1-15929156-3

- Question: Name the number of others votes for when others % is 2.0%
- Gold: `{"sel": 6, "conds": [[5, 0, "2.0%"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "2.0%"]], "sel": 6}`
- Error: logical-form mismatch

## test:1384:1-15945862-1

- Question: What septembers are 17.1 in December? 
- Gold: `{"sel": 12, "conds": [[9, 0, "17.1"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[12, 0, "17.1"]], "sel": 9}`
- Error: logical-form mismatch

## test:1387:1-15945862-1

- Question: January 7.34 where is June ?
- Gold: `{"sel": 1, "conds": [[6, 0, "7.34"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "7.34"]], "sel": 6}`
- Error: logical-form mismatch

## test:1390:1-1601792-3

- Question: What is the frequency of hot fm?
- Gold: `{"sel": 0, "conds": [[1, 0, "Hot FM"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "hot fm"]], "sel": 0}`
- Error: logical-form mismatch

## test:1400:1-1601027-2

- Question: Name the number of headphone class for sr100
- Gold: `{"sel": 1, "conds": [[0, 0, "SR100"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "sr100"]], "sel": 1}`
- Error: logical-form mismatch

## test:1407:1-16034882-4

- Question: What are the total number of losses for the team who has conceded 22?
- Gold: `{"sel": 5, "conds": [[7, 0, 22]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[7, 0, 22]], "sel": 5}`
- Error: logical-form mismatch

## test:1435:1-16308030-1

- Question: How many events have a time of 1:48.322?
- Gold: `{"sel": 1, "conds": [[6, 0, "1:48.322"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[6, 0, "1:48.322"]], "sel": 1}`
- Error: logical-form mismatch

## test:1466:1-1646960-3

- Question: How many winners had a debut album titled "mike"?
- Gold: `{"sel": 1, "conds": [[4, 0, "Mike"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "Mike"]], "sel": 1}`
- Error: logical-form mismatch

## test:1470:1-16457934-5

- Question: If oblast\age is Komis in Nenetskiy Ao, what is the total number of 65 to 69?
- Gold: `{"sel": 13, "conds": [[1, 0, "Komis in Nenetskiy AO"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "Komis in Nenetskiy AO"]], "sel": 13}`
- Error: logical-form mismatch

## test:1475:1-16457934-5

- Question: If 50 to 54 is 2119, what is the total number of c/w 15+?
- Gold: `{"sel": 0, "conds": [[10, 0, 2119]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[10, 0, 2119]], "sel": 0}`
- Error: logical-form mismatch

## test:1483:1-16570286-2

- Question: How many numbers were recorded under matches with Arthur Morris?
- Gold: `{"sel": 2, "conds": [[0, 0, "Arthur Morris"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Arthur Morris"]], "sel": 2}`
- Error: logical-form mismatch

## test:1494:1-16581695-2

- Question: What is the number in series for the episode titled "Kevin's Big Score"?
- Gold: `{"sel": 0, "conds": [[1, 0, "\"Kevin's Big Score\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Kevin's Big Score"]], "sel": 0}`
- Error: logical-form mismatch

## test:1495:1-16581695-2

- Question: Who was the writer of the episode titled "Pier Pressure"?
- Gold: `{"sel": 3, "conds": [[1, 0, "\"Pier Pressure\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Pier Pressure"]], "sel": 3}`
- Error: logical-form mismatch

## test:1497:1-16617011-1

- Question: Name the number air date for 14.20 us viewers
- Gold: `{"sel": 5, "conds": [[6, 0, "14.20"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "14.20"]], "sel": 5}`
- Error: logical-form mismatch

## test:1499:1-16661199-2

- Question: Name the number of giants points for opponents being 31
- Gold: `{"sel": 4, "conds": [[5, 0, 31]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, 31]], "sel": 4}`
- Error: logical-form mismatch

## test:1502:1-16689920-1

- Question: At 1:48.16 what was the number of track time?
- Gold: `{"sel": 7, "conds": [[4, 0, "1:48.16"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "1:48.16"]], "sel": 7}`
- Error: logical-form mismatch

## test:1503:1-16689920-1

- Question: With a date of 8/3/08, what was the length of the victory margin?
- Gold: `{"sel": 5, "conds": [[9, 0, "8/3/08"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[9, 0, "8/3/08"]], "sel": 5}`
- Error: logical-form mismatch

## test:1504:1-16678052-2

- Question: On what date did the opponents win with 17 points? 
- Gold: `{"sel": 1, "conds": [[5, 0, 17], [3, 0, "Win"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Loss"], [5, 0, 17]], "sel": 1}`
- Error: logical-form mismatch

## test:1533:1-1676073-13

- Question: How many losses does Cross Keys RFC have?
- Gold: `{"sel": 4, "conds": [[0, 0, "Cross Keys RFC"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Cross Keys RFC"]], "sel": 4}`
- Error: logical-form mismatch

## test:1538:1-16796625-1

- Question: How many people live in an area of 30.94 hectares?
- Gold: `{"sel": 2, "conds": [[3, 0, "30.94"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "30.94"]], "sel": 2}`
- Error: logical-form mismatch

## test:1542:1-16779068-5

- Question: Name the 3 where weightlifter is m. van der goten ( bel )
- Gold: `{"sel": 9, "conds": [[1, 0, "M. Van der Goten ( BEL )"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "m. van der goten ( bel )"]], "sel": 3}`
- Error: logical-form mismatch

## test:1554:1-16864968-8

- Question: How many people attended the Edmonton Oilers game?
- Gold: `{"sel": 5, "conds": [[2, 0, "Edmonton Oilers"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "Edmonton Oilers"]], "sel": 5}`
- Error: logical-form mismatch

## test:1572:1-17030926-3

- Question: Which season had the "grumpy old bees" episodes?
- Gold: `{"sel": 1, "conds": [[2, 0, "\"Grumpy Old Bees\""]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "\"Grumpy Old Bees\""]], "sel": 1}`
- Error: logical-form mismatch

## test:1573:1-17030926-3

- Question: How many episodes were named "Dogcatcher in the Rye"?
- Gold: `{"sel": 3, "conds": [[2, 0, "\"Dogcatcher in the Rye\""]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "Dogcatcher in the Rye"]], "sel": 0}`
- Error: logical-form mismatch

## test:1588:1-1708050-3

- Question: Name the total number when avg start is 2000
- Gold: `{"sel": 6, "conds": [[0, 0, 2000]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 2000]], "sel": 6}`
- Error: logical-form mismatch

## test:1589:1-1708050-3

- Question: Name the most poles
- Gold: `{"sel": 5, "conds": [], "agg": 2}`
- Prediction: `{"agg": 1, "conds": [], "sel": 5}`
- Error: logical-form mismatch

## test:1597:1-170961-2

- Question: What is the name of the parish where the area is 508.30?
- Gold: `{"sel": 0, "conds": [[2, 0, "508.30"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "508.30"]], "sel": 0}`
- Error: logical-form mismatch

## test:1619:1-171236-2

- Question: What is the population in Westfield?
- Gold: `{"sel": 3, "conds": [[0, 0, "Westfield"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Westfield"]], "sel": 3}`
- Error: logical-form mismatch

## test:1622:1-171236-2

- Question: What is the Area KM 2 of Rothesay?
- Gold: `{"sel": 2, "conds": [[0, 0, "Rothesay"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Rothesay"]], "sel": 2}`
- Error: logical-form mismatch

## test:1638:1-171748-3

- Question: When was the percentage of trains arriving within 5 minutes of scheduled time 89.6%?
- Gold: `{"sel": 0, "conds": [[3, 0, "89.6%"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "89.6%"]], "sel": 0}`
- Error: logical-form mismatch

## test:1653:1-17289224-1

- Question: How many poles did David Price Racing win?
- Gold: `{"sel": 4, "conds": [[2, 0, "David Price Racing"]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "David Price Racing"]], "sel": 4}`
- Error: logical-form mismatch

## test:1658:1-17308269-2

- Question: Name the number of former wnba team for 2
- Gold: `{"sel": 4, "conds": [[0, 0, 2]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 2]], "sel": 4}`
- Error: logical-form mismatch

## test:1697:1-17419587-1

- Question: What is the airport with the IATA MEL?
- Gold: `{"sel": 1, "conds": [[3, 0, "MEL"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "MEL"]], "sel": 1}`
- Error: logical-form mismatch

## test:1703:1-17467147-1

- Question: When "the telenovela" is the title how many series numbers are there?
- Gold: `{"sel": 0, "conds": [[1, 0, "\"The Telenovela\""]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "The Telenovela"]], "sel": 0}`
- Error: logical-form mismatch

## test:1707:1-17481974-1

- Question: Which is the number of the episode "rook gave" "rūku dīo" (デ デ ィ オ ー ル) which aired on July 14, 2003
- Gold: `{"sel": 0, "conds": [[4, 0, "July 14, 2003"]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "\"Rook Dio\" \"Rūku Dīo\" (ルーク·ディーオ)"], [4, 0, "July 14, 2003"]], "sel": 0}`
- Error: logical-form mismatch

## test:1743:1-17632217-2

- Question: What is the total number of clubs when the runner-up was Liaoning Fushun?
- Gold: `{"sel": 6, "conds": [[3, 0, "Liaoning Fushun"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Liaoning Fushun"]], "sel": 6}`
- Error: logical-form mismatch

## test:1750:1-17675675-2

- Question: with the amount of tries at 89, how many win's were there?
- Gold: `{"sel": 2, "conds": [[8, 0, "89"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[8, 0, "89"]], "sel": 2}`
- Error: logical-form mismatch

## test:1752:1-17675675-2

- Question: What is the total amount of points when the given won is 9?
- Gold: `{"sel": 11, "conds": [[2, 0, "9"]], "agg": 0}`
- Prediction: `{"agg": 4, "conds": [[2, 0, "9"]], "sel": 11}`
- Error: logical-form mismatch

## test:1764:1-17779448-1

- Question: How many attended game(s) against the boston patriots?
- Gold: `{"sel": 6, "conds": [[2, 0, "Boston Patriots"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "Boston Patriots"]], "sel": 6}`
- Error: logical-form mismatch

## test:1797:1-18018214-2

- Question: List total loses forh the tauras tauragė team.
- Gold: `{"sel": 5, "conds": [[1, 0, "Tauras Tauragė"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "Tauras Tauragė"]], "sel": 5}`
- Error: logical-form mismatch

## test:1798:1-18018214-2

- Question: List the number of goals scored to equal 58.
- Gold: `{"sel": 7, "conds": [[8, 0, 58]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[8, 0, 58]], "sel": 6}`
- Error: logical-form mismatch

## test:1809:1-18055005-1

- Question: What's the production code of the episode titled "Got to get her out of my house"?
- Gold: `{"sel": 6, "conds": [[2, 0, "\"Got to Get Her Out of My House\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Got to Get Her Out of My House"]], "sel": 6}`
- Error: logical-form mismatch

## test:1810:1-18055005-1

- Question: What's the production code of the episode titled "He ain't a hottie, he's my brother"?
- Gold: `{"sel": 6, "conds": [[2, 0, "\"He Ain't a Hottie, He's My Brother\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "He Ain't a Hottie, He's My Brother"]], "sel": 6}`
- Error: logical-form mismatch

## test:1814:1-18106841-1

- Question: When the trailing votes was 25.88% who was the trailing party?
- Gold: `{"sel": 2, "conds": [[6, 0, "25.88%"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "25.88%"]], "sel": 5}`
- Error: logical-form mismatch

## test:1824:1-18143210-2

- Question: How many 'number of seasons in top division' were played if the 'first season in top division' games is in 1990-91?
- Gold: `{"sel": 2, "conds": [[1, 0, "1990-91"]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "1990-91"]], "sel": 2}`
- Error: logical-form mismatch

## test:1825:1-18143210-2

- Question: How many 'number of season in Liga MX' were played if the 'first season of current spell in top division' is in 1962-63?
- Gold: `{"sel": 4, "conds": [[3, 0, "1962-63"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "1962-63"]], "sel": 4}`
- Error: logical-form mismatch

## test:1830:1-18173916-8

- Question: which episode was Transmitted on wednesday if the episode of "319 sucker punch" was transmitted on tuesday? 
- Gold: `{"sel": 3, "conds": [[2, 0, "319 Sucker Punch"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "319 sucker punch"]], "sel": 3}`
- Error: logical-form mismatch

## test:1833:1-18198579-6

- Question: Name the number of top 10s for scoring rank of 9
- Gold: `{"sel": 6, "conds": [[11, 0, "9"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[11, 0, "9"]], "sel": 6}`
- Error: logical-form mismatch

## test:1835:1-182298-5

- Question: How many are the total winners if 7 won the Men's Open?
- Gold: `{"sel": 5, "conds": [[1, 0, 7]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 0, 7]], "sel": 5}`
- Error: logical-form mismatch

## test:1841:1-18254488-2

- Question: When koki mizuno is the player how man positions are there?
- Gold: `{"sel": 2, "conds": [[1, 0, "Koki Mizuno"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Koki Mizuno"]], "sel": 2}`
- Error: logical-form mismatch

## test:1842:1-18268826-1

- Question: What's the series number for the episode titled "Hunted"?
- Gold: `{"sel": 0, "conds": [[2, 0, "\"Hunted\""]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Hunted"]], "sel": 0}`
- Error: logical-form mismatch

## test:1866:1-18367694-3

- Question: When "c'est la vinnie" is the title what is the air date?
- Gold: `{"sel": 5, "conds": [[2, 0, "\"C'est la Vinnie\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "c'est la vinnie"]], "sel": 5}`
- Error: logical-form mismatch

## test:1867:1-18367694-3

- Question: When "to live and die in brentwood" is the title what is the largest production code?
- Gold: `{"sel": 6, "conds": [[2, 0, "\"To Live and Die in Brentwood\""]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[2, 0, "To Live and Die in Brentwood"]], "sel": 6}`
- Error: logical-form mismatch

## test:1869:1-18428024-3

- Question: How many series did John Banas direct?
- Gold: `{"sel": 0, "conds": [[3, 0, "John Banas"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "John Banas"]], "sel": 0}`
- Error: logical-form mismatch

## test:1870:1-18428024-3

- Question: What is the original air date in series 360?
- Gold: `{"sel": 5, "conds": [[0, 0, 360]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 360]], "sel": 5}`
- Error: logical-form mismatch

## test:1895:1-18569389-1

- Question: Name the total number for number in series that got 3.62 viewers
- Gold: `{"sel": 0, "conds": [[6, 0, "3.62"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[6, 0, "3.62"]], "sel": 0}`
- Error: logical-form mismatch

## test:1906:1-18600760-1

- Question: Name the land for ada
- Gold: `{"sel": 3, "conds": [[0, 0, "Ada"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Ada"]], "sel": 3}`
- Error: logical-form mismatch

## test:1908:1-18597302-1

- Question: What was the position where the team scored 9 points?
- Gold: `{"sel": 0, "conds": [[8, 0, 9]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[8, 0, 9]], "sel": 0}`
- Error: logical-form mismatch

## test:1921:1-18600760-19

- Question: where the land is 35.990 what is the number of the geo id
- Gold: `{"sel": 7, "conds": [[3, 0, "35.990"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "35.990"]], "sel": 7}`
- Error: logical-form mismatch

## test:1945:1-186468-1

- Question: When 4 is the v-band what is the overall amount of ka-bands?
- Gold: `{"sel": 2, "conds": [[4, 0, "4"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[4, 0, 4]], "sel": 2}`
- Error: logical-form mismatch

## test:1954:1-187239-1

- Question: When 2011 is the period and olympikus is the kit manufacturer how many minor sponsors are there?
- Gold: `{"sel": 4, "conds": [[1, 0, "Olympikus"], [0, 0, "2011"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "2011"], [1, 0, "olympikus"]], "sel": 4}`
- Error: logical-form mismatch

## test:1958:1-1876825-6

- Question: In season 5 what episode number was production 06-03-519?
- Gold: `{"sel": 1, "conds": [[6, 0, "06-03-519"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "06-03-519"]], "sel": 1}`
- Error: logical-form mismatch

## test:2021:1-1924975-1

- Question: when the q1+q2 time was 2.34.736, what was the total pos number?
- Gold: `{"sel": 0, "conds": [[7, 0, "2.34.736"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[7, 0, "2.34.736"]], "sel": 0}`
- Error: logical-form mismatch

## test:2029:1-19304764-2

- Question: Name the total number of seats for general surgery
- Gold: `{"sel": 4, "conds": [[0, 0, "General Surgery"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "General Surgery"]], "sel": 2}`
- Error: logical-form mismatch

## test:2035:1-1939214-1

- Question: In what season did the team get in the conference finals of the playoffs?
- Gold: `{"sel": 3, "conds": [[4, 0, "Conference Finals"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "Conference Finals"]], "sel": 0}`
- Error: logical-form mismatch

## test:2042:1-1939367-1

- Question: What is the province amount if the % 2011 is 0.0%
- Gold: `{"sel": 0, "conds": [[4, 0, "0.0%"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "0.0%"]], "sel": 0}`
- Error: logical-form mismatch

## test:2043:1-1939367-1

- Question: If the province is British Columbia, what is the Arabs 2001 total number?
- Gold: `{"sel": 1, "conds": [[0, 0, "British Columbia"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "British Columbia"]], "sel": 1}`
- Error: logical-form mismatch

## test:2053:1-1939405-2

- Question: How many Latin Americans were there in 2001 in the province with 0.0% 2001 and 0.2% 2011?
- Gold: `{"sel": 1, "conds": [[2, 0, "0.0%"], [4, 0, "0.2%"]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "0.0%"], [4, 0, "0.2%"]], "sel": 1}`
- Error: logical-form mismatch

## test:2054:1-1939405-2

- Question: How many Latin Americans lived in 2011 in Saskatchewan?
- Gold: `{"sel": 3, "conds": [[0, 0, "Saskatchewan"]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Saskatchewan"]], "sel": 3}`
- Error: logical-form mismatch

## test:2056:1-1942366-7

- Question: What's the count of pm 10 particles when the pm 2.5 particles are at 59-66?
- Gold: `{"sel": 4, "conds": [[5, 0, "59-66"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[5, 0, "59-66"]], "sel": 4}`
- Error: logical-form mismatch

## test:2058:1-1942366-7

- Question: What's the sulphur dioxide count when the ozone is at 121-140?
- Gold: `{"sel": 3, "conds": [[1, 0, "121-140"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "121-140"]], "sel": 3}`
- Error: logical-form mismatch

## test:2059:1-1942366-7

- Question: What's the sulphur dioxide count when the nitrogen dioxide is 468-534?
- Gold: `{"sel": 3, "conds": [[2, 0, "468-534"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "468-534"]], "sel": 3}`
- Error: logical-form mismatch

## test:2060:1-1942366-7

- Question: What's the nitrogen dioxide count where the sulphur dioxide is at 0-88?
- Gold: `{"sel": 2, "conds": [[3, 0, "0-88"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "0-88"]], "sel": 2}`
- Error: logical-form mismatch

## test:2075:1-19534677-1

- Question: Name the total number for material collected for 978-1401221935
- Gold: `{"sel": 4, "conds": [[6, 0, "978-1401221935"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "978-1401221935"]], "sel": 0}`
- Error: logical-form mismatch

## test:2076:1-19534677-1

- Question: Name the umbr of creators for flash of two worlds
- Gold: `{"sel": 3, "conds": [[2, 0, "Flash of Two Worlds"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "flash of two worlds"]], "sel": 3}`
- Error: logical-form mismatch

## test:2089:1-1965650-10

- Question: What team does Lee Palmer play for?
- Gold: `{"sel": 5, "conds": [[1, 0, "Lee Palmer"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Lee Palmer"]], "sel": 4}`
- Error: logical-form mismatch

## test:2167:1-197638-7

- Question: When was the Australian open?
- Gold: `{"sel": 3, "conds": [], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [], "sel": 3}`
- Error: logical-form mismatch

## test:2181:1-19839391-3

- Question: How many wins had a win percentage of 0.667
- Gold: `{"sel": 2, "conds": [[5, 0, "0.667"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[5, 0, "0.667"]], "sel": 2}`
- Error: logical-form mismatch

## test:2182:1-19839391-3

- Question: how many "no decisions" are there with 3 wins and a win percentage of 1.000?
- Gold: `{"sel": 4, "conds": [[5, 0, "1.000"], [2, 0, 3]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[2, 0, 3], [5, 0, "1.000"]], "sel": 4}`
- Error: logical-form mismatch

## test:2231:1-20142629-2

- Question: where stanier, 2 cylinder is 43, what is the stanier, 3 cylinder
- Gold: `{"sel": 2, "conds": [[3, 0, 43]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, 43]], "sel": 2}`
- Error: logical-form mismatch

## test:2232:1-20142629-2

- Question: When the Fowler is 16, what is the number of cylinders?
- Gold: `{"sel": 2, "conds": [[1, 0, 16]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, 16]], "sel": 2}`
- Error: logical-form mismatch

## test:2238:1-20159025-1

- Question: Who was the driver when the time in part 3 was 1:31.386?
- Gold: `{"sel": 2, "conds": [[4, 0, "1:31.386"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "1:31.386"]], "sel": 2}`
- Error: logical-form mismatch

## test:2240:1-20345624-2

- Question: Name the title that aired on 5 august 1967
- Gold: `{"sel": 3, "conds": [[6, 0, "5 August 1967"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "5 August 1967"]], "sel": 3}`
- Error: logical-form mismatch

## test:2252:1-20367820-16

- Question: How many no outs for an average of 56.38?
- Gold: `{"sel": 5, "conds": [[6, 0, "56.38"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "56.38"]], "sel": 5}`
- Error: logical-form mismatch

## test:2255:1-20396-1

- Question: How many poles were there in season 2000?
- Gold: `{"sel": 5, "conds": [[0, 0, 2000]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 0, 2000]], "sel": 5}`
- Error: logical-form mismatch

## test:2272:1-2064747-1

- Question: What schools are accredited by COE?
- Gold: `{"sel": 1, "conds": [[6, 0, "COE"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "COE"]], "sel": 0}`
- Error: logical-form mismatch

## test:2276:1-2068719-1

- Question: Name the number of δs ‡ /cal mol −1 k −1 for butadiene being 1,2-dimethylene-cyclohexane
- Gold: `{"sel": 4, "conds": [[0, 0, "1,2-dimethylene-cyclohexane"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "1,2-dimethylene-cyclohexane"]], "sel": 4}`
- Error: logical-form mismatch

## test:2298:1-20726262-6

- Question: What episode is titled "Authority Vested"?
- Gold: `{"sel": 1, "conds": [[2, 0, "\"Authority Vested\""]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "\"Authority Vested\""]], "sel": 0}`
- Error: logical-form mismatch

## test:2300:1-20726262-6

- Question: What episode was directed by Karen Gaviola?
- Gold: `{"sel": 1, "conds": [[3, 0, "Karen Gaviola"]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Karen Gaviola"]], "sel": 2}`
- Error: logical-form mismatch

## test:2306:1-20745746-1

- Question: How many games resulted in a loss?
- Gold: `{"sel": 0, "conds": [[6, 0, "Loss"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[6, 0, "Loss"]], "sel": 0}`
- Error: logical-form mismatch

## test:2320:1-20754016-2

- Question: How tall is the contestant from Guatemala?
- Gold: `{"sel": 3, "conds": [[0, 0, "Guatemala"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Guatemala"]], "sel": 4}`
- Error: logical-form mismatch

## test:2323:1-2076463-2

- Question: What is the only type of university that was founded in 1873?
- Gold: `{"sel": 2, "conds": [[5, 0, 1873]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, 1873]], "sel": 3}`
- Error: logical-form mismatch

## test:2326:1-2076463-2

- Question: What type of school would you see when visiting Missouri Western State University?
- Gold: `{"sel": 2, "conds": [[0, 0, "Missouri Western State University"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Missouri Western State University"]], "sel": 3}`
- Error: logical-form mismatch

## test:2353:1-20819379-2

- Question: Name the total number of tie number for team 2 osijek
- Gold: `{"sel": 0, "conds": [[3, 0, "Osijek"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[3, 0, "Osijek"]], "sel": 0}`
- Error: logical-form mismatch

## test:2360:1-20855452-4

- Question: What was the max when they score 2200?
- Gold: `{"sel": 5, "conds": [[2, 0, 2200]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[2, 0, 2200]], "sel": 0}`
- Error: logical-form mismatch

## test:2362:1-20855452-4

- Question: How many points did shahar pe'er score?
- Gold: `{"sel": 4, "conds": [[1, 0, "Shahar Pe'er"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Shahar Pe'er"]], "sel": 2}`
- Error: logical-form mismatch

## test:2366:1-20872722-1

- Question: What is the round?
- Gold: `{"sel": 0, "conds": [], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [], "sel": 0}`
- Error: logical-form mismatch

## test:2367:1-20872722-1

- Question: What is the height of the cornerback position?
- Gold: `{"sel": 4, "conds": [[3, 0, "Cornerback"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Cornerback"]], "sel": 4}`
- Error: logical-form mismatch

## test:2373:1-20887670-1

- Question: in what year did the colors red and gold join?
- Gold: `{"sel": 2, "conds": [[6, 0, "Red and Gold"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "Red and Gold"]], "sel": 2}`
- Error: logical-form mismatch

## test:2392:1-20971444-3

- Question: Name the episode for 18-49 rating being 3.6
- Gold: `{"sel": 0, "conds": [[2, 0, "3.6"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "3.6"]], "sel": 0}`
- Error: logical-form mismatch

## test:2395:1-20971444-3

- Question: Name the rank timeslot for 18-49 share being 13
- Gold: `{"sel": 5, "conds": [[3, 0, 13]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, 13]], "sel": 5}`
- Error: logical-form mismatch

## test:2397:1-20971444-3

- Question: Name the total number for 18-49 share being 18-49 being 3.1
- Gold: `{"sel": 3, "conds": [[2, 0, "3.1"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "3.1"]], "sel": 3}`
- Error: logical-form mismatch

## test:2423:1-21132404-1

- Question: How many seats in 2006 has a % 1997 rating of 38.9?
- Gold: `{"sel": 2, "conds": [[5, 0, "38.9"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "38.9"]], "sel": 2}`
- Error: logical-form mismatch

## test:2434:1-21258-1

- Question: where births is 388 000 how many number is natural increase
- Gold: `{"sel": 6, "conds": [[1, 0, "388 000"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "388 000"]], "sel": 6}`
- Error: logical-form mismatch

## test:2456:1-21422977-1

- Question: When nº is 3, what are all the ministires?
- Gold: `{"sel": 7, "conds": [[0, 0, 3]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 3]], "sel": 7}`
- Error: logical-form mismatch

## test:2483:1-21636599-1

- Question: How many security forces?
- Gold: `{"sel": 2, "conds": [], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [], "sel": 2}`
- Error: logical-form mismatch

## test:2484:1-21636599-1

- Question: How many insurgents have 2003 as a period?
- Gold: `{"sel": 3, "conds": [[0, 0, "2003"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "2003"]], "sel": 3}`
- Error: logical-form mismatch

## test:2488:1-2169966-2

- Question: What was his average finish when his average start was 27.7?
- Gold: `{"sel": 7, "conds": [[6, 0, "27.7"]], "agg": 0}`
- Prediction: `{"agg": 5, "conds": [[6, 0, "27.7"]], "sel": 7}`
- Error: logical-form mismatch

## test:2497:1-2175685-1

- Question: How many miles (km) were driven when the average speed (mph) was 103.145?
- Gold: `{"sel": 6, "conds": [[8, 0, "103.145"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[8, 0, "103.145"]], "sel": 6}`
- Error: logical-form mismatch

## test:2501:1-21795650-1

- Question: What is the point total for the Formula Renault 2.0 Italy series?
- Gold: `{"sel": 8, "conds": [[1, 0, "Formula Renault 2.0 Italy"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Formula Renault 2.0 Italy"]], "sel": 8}`
- Error: logical-form mismatch

## test:2513:1-2182573-2

- Question: How many poles were there in 1996?
- Gold: `{"sel": 5, "conds": [[0, 0, 1996]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[0, 0, 1996]], "sel": 5}`
- Error: logical-form mismatch

## test:2517:1-2190919-3

- Question: If the winnings was $250,667, what is the top 5 total number?
- Gold: `{"sel": 3, "conds": [[8, 0, "$250,667"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[8, 0, "$250,667"]], "sel": 3}`
- Error: logical-form mismatch

## test:2524:1-2196127-1

- Question: How many laps were there in 2002?
- Gold: `{"sel": 5, "conds": [[0, 0, "2002"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "2002"]], "sel": 5}`
- Error: logical-form mismatch

## test:2530:1-21995420-6

- Question: How many stunts have a total of 201.5?
- Gold: `{"sel": 4, "conds": [[8, 0, "201.5"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[8, 0, "201.5"]], "sel": 4}`
- Error: logical-form mismatch

## test:2549:1-22056184-1

- Question: How many poles when British formula renault 2.0 series and f/laps 1?
- Gold: `{"sel": 5, "conds": [[1, 0, "British Formula Renault 2.0"], [6, 0, 1]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "British Formula Renault 2.0"], [6, 0, 1]], "sel": 5}`
- Error: logical-form mismatch

## test:2550:1-22056184-1

- Question: How many points when pole are 1?
- Gold: `{"sel": 8, "conds": [[5, 0, 1]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[5, 0, 1]], "sel": 8}`
- Error: logical-form mismatch

## test:2552:1-22058547-1

- Question: How many high schools have storm mascots?
- Gold: `{"sel": 0, "conds": [[4, 0, "Storm"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "Storm"]], "sel": 0}`
- Error: logical-form mismatch

## test:2554:1-22058547-1

- Question: What school classifications have trappers as mascot?
- Gold: `{"sel": 1, "conds": [[4, 0, "Trappers"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "Trappers"]], "sel": 5}`
- Error: logical-form mismatch

## test:2562:1-221398-1

- Question: How many prefectures have a population density of 16 people/kilometers squared?
- Gold: `{"sel": 4, "conds": [[0, 0, "16"]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "16"]], "sel": 1}`
- Error: logical-form mismatch

## test:2566:1-2216245-2

- Question: How many top 5s when he was on team #28/#49 jay robinson racing?
- Gold: `{"sel": 3, "conds": [[10, 0, "#28/#49 Jay Robinson Racing"]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[10, 0, "#28/#49 Jay Robinson Racing"]], "sel": 3}`
- Error: logical-form mismatch

## test:2568:1-2221484-2

- Question: Who directed "loathe and marriage"?
- Gold: `{"sel": 3, "conds": [[2, 0, "\"Loathe and Marriage\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "loathe and marriage"]], "sel": 3}`
- Error: logical-form mismatch

## test:2581:1-22265225-1

- Question: What episode number in the series was "igo nuclear"?
- Gold: `{"sel": 1, "conds": [[2, 0, "\"iGo Nuclear\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "igo nuclear"]], "sel": 0}`
- Error: logical-form mismatch

## test:2583:1-22265225-1

- Question: How many million U.s. Viewers watched episode 12 in the season?
- Gold: `{"sel": 7, "conds": [[1, 0, "12"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "12"]], "sel": 7}`
- Error: logical-form mismatch

## test:2586:1-22265261-1

- Question: What was the Sp of the 2nd Position?
- Gold: `{"sel": 5, "conds": [[0, 0, "2nd"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "2nd"]], "sel": 5}`
- Error: logical-form mismatch

## test:2587:1-22265261-1

- Question: How old was the horse when the SP was 200/1?
- Gold: `{"sel": 3, "conds": [[5, 0, "200/1"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "200/1"]], "sel": 3}`
- Error: logical-form mismatch

## test:2593:1-2226817-6

- Question: When did the episode titled "Route 666 (part 1)" air for the first time?
- Gold: `{"sel": 5, "conds": [[2, 0, "\"Route 666 (Part 1)\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Route 666 (part 1)"]], "sel": 5}`
- Error: logical-form mismatch

## test:2612:1-22355-71

- Question: How many silver medalist was won?
- Gold: `{"sel": 5, "conds": [], "agg": 1}`
- Prediction: `{"agg": 4, "conds": [], "sel": 5}`
- Error: logical-form mismatch

## test:2629:1-22496344-1

- Question: What is the # when conroe, tx is the hometown?
- Gold: `{"sel": 1, "conds": [[6, 0, "Conroe, TX"]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "Conroe, TX"]], "sel": 1}`
- Error: logical-form mismatch

## test:2632:1-22496344-1

- Question: What is the # for worthing high school?
- Gold: `{"sel": 1, "conds": [[7, 0, "Worthing"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[7, 0, "Worthing"]], "sel": 1}`
- Error: logical-form mismatch

## test:2633:1-225094-4

- Question: Name the reason for change for jonathan jennings
- Gold: `{"sel": 2, "conds": [[3, 0, "Jonathan Jennings"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Jonathan Jennings"]], "sel": 2}`
- Error: logical-form mismatch

## test:2686:1-22667773-8

- Question: Name the number of ends for cardiff city and df
- Gold: `{"sel": 9, "conds": [[11, 0, "Cardiff City"], [1, 0, "DF"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[11, 0, "Cardiff City"], [1, 0, "DF"]], "sel": 9}`
- Error: logical-form mismatch

## test:2697:1-22670216-1

- Question: If the location is Brooklyn, Michigan and the pole position is Bobby Unser, what is the RND total number?
- Gold: `{"sel": 0, "conds": [[5, 0, "Brooklyn, Michigan"], [6, 0, "Bobby Unser"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[5, 0, "Brooklyn , Michigan"], [6, 0, "Bobby Unser"]], "sel": 0}`
- Error: logical-form mismatch

## test:2698:1-22670216-1

- Question: If the pole position is Johnny Rutherford and the track is the Ontario Motor Speedway, what is the RND total number?
- Gold: `{"sel": 0, "conds": [[4, 0, "Ontario Motor Speedway"], [6, 0, "Johnny Rutherford"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[6, 0, "Johnny Rutherford"], [4, 0, "Ontario Motor Speedway"]], "sel": 0}`
- Error: logical-form mismatch

## test:2704:1-22756549-1

- Question: What party is the winner K. Anbazhagan from?
- Gold: `{"sel": 5, "conds": [[1, 0, "K. Anbazhagan"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "K. Anbazhagan"]], "sel": 2}`
- Error: logical-form mismatch

## test:2712:1-22815568-7

- Question: What is the unemployment rate in those places where the market income per capita is $16,981?
- Gold: `{"sel": 2, "conds": [[3, 0, "$16,981"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "$16,981"]], "sel": 2}`
- Error: logical-form mismatch

## test:2727:1-22848931-3

- Question: Name the outgoing manager for 10 june 2009
- Gold: `{"sel": 1, "conds": [[3, 0, "10 June 2009"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "10 June 2009"]], "sel": 1}`
- Error: logical-form mismatch

## test:2744:1-22916979-2

- Question: which area has a rank of 60?
- Gold: `{"sel": 2, "conds": [[0, 0, 60]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 60]], "sel": 1}`
- Error: logical-form mismatch

## test:2761:1-23018775-3

- Question: How many lap two's did marco andretti do?
- Gold: `{"sel": 5, "conds": [[2, 0, "Marco Andretti"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Marco Andretti"]], "sel": 5}`
- Error: logical-form mismatch

## test:2781:1-231623-3

- Question: Name the growth rate for density of 1087
- Gold: `{"sel": 3, "conds": [[6, 0, 1087]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[6, 0, 1087]], "sel": 3}`
- Error: logical-form mismatch

## test:2841:1-23285761-11

- Question: How many teams have channing frye, jason richardson (8) as high rebounds?
- Gold: `{"sel": 2, "conds": [[5, 0, "Channing Frye, Jason Richardson (8)"]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[5, 0, "Channing Frye , Jason Richardson (8)"]], "sel": 2}`
- Error: logical-form mismatch

## test:2865:1-23289934-1

- Question: Name the least number for production code for 3abc21
- Gold: `{"sel": 0, "conds": [[6, 0, "3ABC21"]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[6, 0, "3abc21"]], "sel": 1}`
- Error: logical-form mismatch

## test:2875:1-23308178-8

- Question: How many games did they play on february 5?
- Gold: `{"sel": 2, "conds": [[1, 0, "February 5"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "February 5"]], "sel": 0}`
- Error: logical-form mismatch

## test:2899:1-23483182-1

- Question: What number was there 6.01 million u.s. drivers?
- Gold: `{"sel": 1, "conds": [[5, 0, "6.01"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "6.01"]], "sel": 0}`
- Error: logical-form mismatch

## test:2907:1-23528223-2

- Question: Who directed the episode titled "Redemptio"?
- Gold: `{"sel": 3, "conds": [[2, 0, "\"Redemptio\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Redemptio"]], "sel": 3}`
- Error: logical-form mismatch

## test:2908:1-23575917-2

- Question: Name the scores for  david baddiel and maureen lipman
- Gold: `{"sel": 4, "conds": [[2, 0, "David Baddiel and Maureen Lipman"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "David Baddiel and Maureen Lipman"]], "sel": 4}`
- Error: logical-form mismatch

## test:2915:1-23575917-7

- Question: If the episode is 6x03, what is the first broadcast total number?
- Gold: `{"sel": 1, "conds": [[0, 0, "6x03"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "6x03"]], "sel": 1}`
- Error: logical-form mismatch

## test:2916:1-23575917-7

- Question: If the lees team is Clare Balding and Miranda Hart, what is the first broadcast total number?
- Gold: `{"sel": 1, "conds": [[3, 0, "Clare Balding and Miranda Hart"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Clare Balding and Miranda Hart"]], "sel": 1}`
- Error: logical-form mismatch

## test:2919:1-23585197-3

- Question: What is the position of "kärleken vänder allt" (the love turns everything)?
- Gold: `{"sel": 3, "conds": [[1, 0, "\"Kärleken vänder allt\" (The love turns everything)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "kärleken vänder allt"]], "sel": 3}`
- Error: logical-form mismatch

## test:2923:1-23585197-3

- Question: What is the position of "kärleken vänder allt" (the love turns everything)?
- Gold: `{"sel": 3, "conds": [[1, 0, "\"Kärleken vänder allt\" (The love turns everything)"]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "kärleken vänder allt"]], "sel": 3}`
- Error: logical-form mismatch

## test:2949:1-23799417-1

- Question: What was the original airdate for "Something New"?
- Gold: `{"sel": 5, "conds": [[2, 0, "\"Something New\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Something New"]], "sel": 5}`
- Error: logical-form mismatch

## test:2955:1-238124-1

- Question: What is the prothrombin time of von willebrand disease? 
- Gold: `{"sel": 1, "conds": [[0, 0, "Von Willebrand disease"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Von Willebrand disease"]], "sel": 1}`
- Error: logical-form mismatch

## test:2966:1-23851574-2

- Question: Which aperture were built or used between 1987-2001?
- Gold: `{"sel": 2, "conds": [[6, 0, "1987-2001"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "1987-2001"]], "sel": 1}`
- Error: logical-form mismatch

## test:2979:1-23963073-1

- Question: How many English translations were made for the story originally titled "La Ribambelle Enquête"?
- Gold: `{"sel": 2, "conds": [[0, 0, "\"La Ribambelle enquête\""]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "La Ribambelle Enquête"]], "sel": 2}`
- Error: logical-form mismatch

## test:2980:1-23963073-1

- Question: What was the English translation of "La Ribambelle Aux Galopingos"?
- Gold: `{"sel": 2, "conds": [[0, 0, "\"La Ribambelle aux Galopingos\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "La Ribambelle Aux Galopingos"]], "sel": 2}`
- Error: logical-form mismatch

## test:2990:1-2409041-4

- Question: Name the number of number in the season for 11
- Gold: `{"sel": 0, "conds": [[1, 0, 11]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[0, 0, 11]], "sel": 1}`
- Error: logical-form mismatch

## test:3000:1-24115349-6

- Question: How many votes for brown in the place that had 84.1% for coakley?
- Gold: `{"sel": 3, "conds": [[2, 0, "84.1%"]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "84.1%"]], "sel": 3}`
- Error: logical-form mismatch

## test:3027:1-24223834-3

- Question: How may overall episodes had the title "this is what they want"?
- Gold: `{"sel": 0, "conds": [[2, 0, "This is What They Want"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "This is What They Want"]], "sel": 0}`
- Error: logical-form mismatch

## test:3049:1-24431348-18

- Question: What the total amount of points won during seed 25?
- Gold: `{"sel": 5, "conds": [[0, 0, 25]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 0, 25]], "sel": 5}`
- Error: logical-form mismatch

## test:3053:1-24431264-17

- Question: List the total defensive points for marion bartoli.
- Gold: `{"sel": 4, "conds": [[2, 0, "Marion Bartoli"]], "agg": 0}`
- Prediction: `{"agg": 4, "conds": [[2, 0, "Marion Bartoli"]], "sel": 4}`
- Error: logical-form mismatch

## test:3054:1-24431264-17

- Question: List the competitor ranking with 900 defense points.
- Gold: `{"sel": 0, "conds": [[4, 0, "900"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "900"]], "sel": 1}`
- Error: logical-form mismatch

## test:3055:1-24431264-17

- Question: How many new defense points over 280 did agnieszka radwańska score?
- Gold: `{"sel": 6, "conds": [[4, 0, "280"], [2, 0, "Agnieszka Radwańska"]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[4, 1, 280], [2, 0, "Agnieszka Radwańska"]], "sel": 6}`
- Error: logical-form mismatch

## test:3060:1-24431264-18

- Question: List the rank of the player that left the tournament due to right foot injury
- Gold: `{"sel": 0, "conds": [[6, 0, "right foot injury"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "right foot injury"]], "sel": 0}`
- Error: logical-form mismatch

## test:3077:1-24475186-2

- Question: What ends lost came out to 37?
- Gold: `{"sel": 9, "conds": [[7, 0, 37]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[7, 0, 37]], "sel": 7}`
- Error: logical-form mismatch

## test:3078:1-24475186-2

- Question: How many skips ended where the ends lost was 46?
- Gold: `{"sel": 1, "conds": [[7, 0, 46]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[7, 0, 46]], "sel": 1}`
- Error: logical-form mismatch

## test:3079:1-24475186-2

- Question: How many ends won were smaller than 46.0?
- Gold: `{"sel": 2, "conds": [[6, 2, 46.0]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[6, 2, 46.0]], "sel": 6}`
- Error: logical-form mismatch

## test:3084:1-2453243-4

- Question: When "sheep thrills" is the title what is the air date?
- Gold: `{"sel": 5, "conds": [[2, 0, "\"Sheep Thrills\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Sheep Thrills"]], "sel": 5}`
- Error: logical-form mismatch

## test:3092:1-24565004-8

- Question: What is the number of goals if the name is Xavier Gravelaine?
- Gold: `{"sel": 4, "conds": [[0, 0, "Xavier Gravelaine"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Xavier Gravelaine"]], "sel": 4}`
- Error: logical-form mismatch

## test:3104:1-24625467-1

- Question: Who directed "hey now hey now perry'S girlfriend's back"?
- Gold: `{"sel": 2, "conds": [[1, 0, "\"Hey Now Hey Now Perry's Girlfriend's Back\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Hey Now Hey Now Perry's Girlfriend's Back"]], "sel": 2}`
- Error: logical-form mismatch

## test:3118:1-2468961-3

- Question: What was the original air date of "The Boss"?
- Gold: `{"sel": 5, "conds": [[2, 0, "\"The Boss\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "The Boss"]], "sel": 5}`
- Error: logical-form mismatch

## test:3160:1-24887326-7

- Question: When the away team is Millwall, what is the total possible amount of tie numbers?
- Gold: `{"sel": 0, "conds": [[3, 0, "Millwall"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[3, 0, "Millwall"]], "sel": 0}`
- Error: logical-form mismatch

## test:3162:1-24910742-1

- Question: Who directed the episode entitled "Shotgun"?
- Gold: `{"sel": 3, "conds": [[2, 0, "\"Shotgun\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Shotgun"]], "sel": 3}`
- Error: logical-form mismatch

## test:3183:1-24990183-5

- Question: What was the 09-10 oi best of the player with 949 points?
- Gold: `{"sel": 7, "conds": [[1, 0, 949]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, 949]], "sel": 7}`
- Error: logical-form mismatch

## test:3196:1-2501754-4

- Question: What was the production count of "The Mayor of Northolt"?
- Gold: `{"sel": 1, "conds": [[4, 0, "\"The Mayor Of Northolt\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "The Mayor Of Northolt"]], "sel": 1}`
- Error: logical-form mismatch

## test:3197:1-2501754-3

- Question: What is the production number for the episode named "mine’s a double"?
- Gold: `{"sel": 1, "conds": [[4, 0, "\"Mine’s A Double\""]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "Mine’s A Double"]], "sel": 1}`
- Error: logical-form mismatch

## test:3199:1-2501754-3

- Question: List the 1st air date for the episode titled "baby talk".
- Gold: `{"sel": 2, "conds": [[4, 0, "\"Baby Talk\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "Baby Talk"]], "sel": 2}`
- Error: logical-form mismatch

## test:3211:1-25042332-16

- Question: What percentage of the population is below 50% of the median income in the region where 10.4% of the population earns below 40% of the median income?
- Gold: `{"sel": 3, "conds": [[2, 0, "10.4%"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "10.4%"]], "sel": 3}`
- Error: logical-form mismatch

## test:3244:1-2517159-1

- Question: Name the name of bowl for 2006 season
- Gold: `{"sel": 0, "conds": [[3, 0, "2006 Season"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "2006 Season"]], "sel": 0}`
- Error: logical-form mismatch

## test:3247:1-2517159-1

- Question: Name the appearance for independence bowl
- Gold: `{"sel": 2, "conds": [[0, 0, "Independence Bowl"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "independence bowl"]], "sel": 2}`
- Error: logical-form mismatch

## test:3253:1-25256368-1

- Question: Name the bed 2010 for 6.5%
- Gold: `{"sel": 2, "conds": [[6, 0, "6.5%"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "6.5%"]], "sel": 0}`
- Error: logical-form mismatch

## test:3266:1-25345002-1

- Question: What are the dates of death of those politicians whose date of birth 1938-08-30 30 august 1938?
- Gold: `{"sel": 8, "conds": [[2, 0, "1938-08-30 30 August 1938"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "1938-08-30 30 August 1938"]], "sel": 8}`
- Error: logical-form mismatch

## test:3267:1-2534387-11

- Question: If the event number is 5, what is the winner total number?
- Gold: `{"sel": 4, "conds": [[2, 0, 5]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, 5]], "sel": 4}`
- Error: logical-form mismatch

## test:3309:1-25563779-4

- Question: If the national trophy/rookie is Simone Iaquinta, what is the season total number?
- Gold: `{"sel": 0, "conds": [[5, 0, "Simone Iaquinta"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[5, 0, "Simone Iaquinta"]], "sel": 0}`
- Error: logical-form mismatch

## test:3316:1-25594271-2

- Question: How many LOA metres were there when the corrected time d:hh:mm:ss is 4:03:13:38?
- Gold: `{"sel": 5, "conds": [[7, 0, "4:03:13:38"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[7, 0, "4:03:13:38"]], "sel": 5}`
- Error: logical-form mismatch

## test:3319:1-25594271-2

- Question: How many LOA metres were there when the skipper is lou abrahams?
- Gold: `{"sel": 5, "conds": [[6, 0, "Lou Abrahams"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[6, 0, "Lou Abrahams"]], "sel": 5}`
- Error: logical-form mismatch

## test:3323:1-25604014-8

- Question: What episode number in the season is "parent trap"?
- Gold: `{"sel": 1, "conds": [[2, 0, "\"Parent Trap\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "parent trap"]], "sel": 1}`
- Error: logical-form mismatch

## test:3331:1-2562572-22

- Question: Name the population for kolut
- Gold: `{"sel": 3, "conds": [[0, 0, "Kolut"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Kolut"]], "sel": 3}`
- Error: logical-form mismatch

## test:3334:1-2562572-20

- Question: Name the number of population for  врбас
- Gold: `{"sel": 3, "conds": [[1, 0, "Врбас"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Врбас"]], "sel": 3}`
- Error: logical-form mismatch

## test:3342:1-2562572-35

- Question: Name the population 2011 for mihajlovo
- Gold: `{"sel": 3, "conds": [[0, 0, "Mihajlovo"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Mihajlovo"]], "sel": 3}`
- Error: logical-form mismatch

## test:3344:1-2562572-35

- Question: Name the total number of population 2011 for perlez
- Gold: `{"sel": 3, "conds": [[0, 0, "Perlez"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Perlez"]], "sel": 3}`
- Error: logical-form mismatch

## test:3364:1-25640730-7

- Question: If the director is Yannick Bisson, what was the Canadian amount of viewers?
- Gold: `{"sel": 7, "conds": [[3, 0, "Yannick Bisson"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Yannick Bisson"]], "sel": 7}`
- Error: logical-form mismatch

## test:3389:1-25696729-8

- Question: What is the highest rebound  Dennis Rodman obtained within the 20 rebounds category given two of the following:points, rebounds, assists, steals, and blocked shots (points) greater equal to 5
- Gold: `{"sel": 2, "conds": [[5, 0, 5]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[2, 3, 5]], "sel": 6}`
- Error: operator 3 is not executable

## test:3394:1-25703-2

- Question: What is the total number of birth/2012 for January–December 2012 in Kurgan Oblast?
- Gold: `{"sel": 1, "conds": [[0, 0, "Kurgan Oblast"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "Kurgan Oblast"]], "sel": 1}`
- Error: logical-form mismatch

## test:3399:1-25714995-2

- Question: How many l's are there for the skip with 3 for w? 
- Gold: `{"sel": 2, "conds": [[1, 0, 3]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[1, 0, 3]], "sel": 2}`
- Error: logical-form mismatch

## test:3405:1-25718552-2

- Question: How many ends were won where the blank ends are smaller than 3.0?
- Gold: `{"sel": 5, "conds": [[7, 2, 3.0]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[7, 2, 3.0]], "sel": 5}`
- Error: logical-form mismatch

## test:3416:1-25737761-4

- Question: How many items are listed under the column 'viewing figure' for "the looking glass"?
- Gold: `{"sel": 6, "conds": [[2, 0, "\"The Looking Glass\""]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "The Looking Glass"]], "sel": 6}`
- Error: logical-form mismatch

## test:3436:1-25800134-11

- Question: Who directed the episode with a title of " old friend "?
- Gold: `{"sel": 3, "conds": [[2, 0, "\" Old Friend \""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "old friend"]], "sel": 3}`
- Error: logical-form mismatch

## test:3437:1-25800134-12

- Question: What episode  number of the series aired on February 26, 1968?
- Gold: `{"sel": 0, "conds": [[5, 0, "February 26, 1968"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "February 26, 1968"]], "sel": 1}`
- Error: logical-form mismatch

## test:3455:1-25923164-1

- Question: What was the original air date of "unprepared"?
- Gold: `{"sel": 4, "conds": [[1, 0, "\"Unprepared\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Unprepared"]], "sel": 4}`
- Error: logical-form mismatch

## test:3459:1-25923164-1

- Question: Who wrote the episode "crash"?
- Gold: `{"sel": 3, "conds": [[1, 0, "\"Crash\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Crash"]], "sel": 3}`
- Error: logical-form mismatch

## test:3473:1-26130295-3

- Question: who is first team when dimitris diamantidis play.
- Gold: `{"sel": 2, "conds": [[0, 0, "Dimitris Diamantidis"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "dimitris diamantidis"]], "sel": 2}`
- Error: logical-form mismatch

## test:3476:1-26129220-2

- Question: How many party classifications are there for the senator from Canton? 
- Gold: `{"sel": 2, "conds": [[3, 0, "Canton"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "Canton"]], "sel": 2}`
- Error: logical-form mismatch

## test:3486:1-26139378-1

- Question: What is the original airdate of the episode titled "Taking it on the Chin"?
- Gold: `{"sel": 5, "conds": [[2, 0, "\"Taking It on the Chin\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Taking It on the Chin"]], "sel": 5}`
- Error: logical-form mismatch

## test:3489:1-26139378-1

- Question: What number in the series episode was titled "Puppy Love"?
- Gold: `{"sel": 1, "conds": [[2, 0, "\"Puppy Love\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Puppy Love"]], "sel": 1}`
- Error: logical-form mismatch

## test:3492:1-26168687-5

- Question: Name the most number in season 
- Gold: `{"sel": 1, "conds": [], "agg": 2}`
- Prediction: `{"agg": 1, "conds": [], "sel": 1}`
- Error: logical-form mismatch

## test:3506:1-26202812-7

- Question: Which match was the final score 7–6 (7–0) , 6–7 (5–7) , 4–6, 6–2, 6–7 (5–7)?
- Gold: `{"sel": 1, "conds": [[6, 0, "7–6 (7–0) , 6–7 (5–7) , 4–6, 6–2, 6–7 (5–7)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "7–6 (7–0) , 6–7 (5–7) , 4–6, 6–2, 6–7 (5–7)"]], "sel": 3}`
- Error: logical-form mismatch

## test:3518:1-26223231-1

- Question: How many championships are there when there are 6 points
- Gold: `{"sel": 1, "conds": [[8, 0, "6"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[8, 0, "6"]], "sel": 1}`
- Error: logical-form mismatch

## test:3519:1-26223231-1

- Question: When there are 2 wins, how many poles are?
- Gold: `{"sel": 5, "conds": [[4, 0, 2]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 0, 2]], "sel": 5}`
- Error: logical-form mismatch

## test:3536:1-26263954-1

- Question: how many revised hepburn when english is roman characters
- Gold: `{"sel": 3, "conds": [[0, 0, "Roman characters"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "roman characters"]], "sel": 3}`
- Error: logical-form mismatch

## test:3539:1-26263954-1

- Question: how many kana spelling when english is mount fuji 
- Gold: `{"sel": 2, "conds": [[0, 0, "Mount Fuji"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "mount fuji"]], "sel": 2}`
- Error: logical-form mismatch

## test:3540:1-26263954-1

- Question: when english is tea how many nihon-shiki
- Gold: `{"sel": 5, "conds": [[0, 0, "tea"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "tea"]], "sel": 5}`
- Error: logical-form mismatch

## test:3543:1-26293875-3

- Question: What episode number was "Stumped Again / The Kick Stays in the Picture"?
- Gold: `{"sel": 1, "conds": [[2, 0, "\"Stumped Again / The Kick Stays in the Picture\""]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Stumped Again / The Kick Stays in the Picture"]], "sel": 0}`
- Error: logical-form mismatch

## test:3549:1-26351260-1

- Question: How many school teams are nicknamed "Bulldogs".
- Gold: `{"sel": 1, "conds": [[5, 0, "Bulldogs"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[5, 0, "Bulldogs"]], "sel": 0}`
- Error: logical-form mismatch

## test:3563:1-26397277-3

- Question: Name the employee real name for raw and superstar
- Gold: `{"sel": 2, "conds": [[4, 0, "Raw"], [3, 0, "Superstar"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "raw"], [3, 0, "superstar"]], "sel": 2}`
- Error: logical-form mismatch

## test:3567:1-26400438-1

- Question: In how many races did he have 8 podium finishes?
- Gold: `{"sel": 3, "conds": [[7, 0, 8]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[7, 0, 8]], "sel": 3}`
- Error: logical-form mismatch

## test:3587:1-2655016-9

- Question: what is the series number of the "harry bladder special"?
- Gold: `{"sel": 1, "conds": [[2, 0, "\"Harry Bladder Special\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Harry Bladder Special"]], "sel": 1}`
- Error: logical-form mismatch

## test:3639:1-26744350-2

- Question: How many episodes have the title "revenge of the mummy"?
- Gold: `{"sel": 4, "conds": [[1, 0, "\"Revenge of the Mummy\""]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "Revenge of the Mummy"]], "sel": 0}`
- Error: logical-form mismatch

## test:3662:1-2679061-7

- Question: Where are the Buffalo Sabres from?
- Gold: `{"sel": 5, "conds": [[4, 0, "Buffalo Sabres"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "Buffalo Sabres"]], "sel": 3}`
- Error: logical-form mismatch

## test:3663:1-26804862-1

- Question: When "the legacy" is the title what is the production code?
- Gold: `{"sel": 6, "conds": [[2, 0, "\"The Legacy\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "the legacy"]], "sel": 6}`
- Error: logical-form mismatch

## test:3667:1-26808178-1

- Question: How many million viewers watched episode 3 in the series?
- Gold: `{"sel": 5, "conds": [[0, 0, 3]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 0, 3]], "sel": 5}`
- Error: logical-form mismatch

## test:3668:1-26808178-1

- Question: Who wrote "pocket pussy"?
- Gold: `{"sel": 3, "conds": [[1, 0, "\"Pocket Pussy\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Pocket Pussy"]], "sel": 3}`
- Error: logical-form mismatch

## test:3675:1-26853172-1

- Question: What is the hand number of the hand where player 1 is south and the east wind is prevailing?
- Gold: `{"sel": 0, "conds": [[2, 0, "South"], [1, 0, "East"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "South"], [1, 0, "East"]], "sel": 0}`
- Error: logical-form mismatch

## test:3712:1-27115960-1

- Question: Title is the total number where u.s. viewers (million) is 7.56.
- Gold: `{"sel": 1, "conds": [[6, 0, "7.56"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "7.56"]], "sel": 1}`
- Error: logical-form mismatch

## test:3816:1-27615896-18

- Question: How many points were won where new points was 1680?
- Gold: `{"sel": 5, "conds": [[6, 0, 1680]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[6, 0, 1680]], "sel": 5}`
- Error: logical-form mismatch

## test:3828:1-27666856-3

- Question: Name the date of appointment for 26 may 2011
- Gold: `{"sel": 5, "conds": [[3, 0, "26 May 2011"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "26 May 2011"]], "sel": 5}`
- Error: logical-form mismatch

## test:3829:1-27666856-3

- Question: Name the outgoing manager for esteban vigo
- Gold: `{"sel": 1, "conds": [[4, 0, "Esteban Vigo"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "Esteban Vigo"]], "sel": 1}`
- Error: logical-form mismatch

## test:3843:1-2771237-1

- Question: How many times was the overall attendance 17807?
- Gold: `{"sel": 3, "conds": [[4, 0, 17807]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[3, 0, 17807]], "sel": 3}`
- Error: logical-form mismatch

## test:3898:1-27765443-2

- Question: Name the number of processors for nec sx-4 vector processor
- Gold: `{"sel": 2, "conds": [[1, 0, "NEC SX-4 vector processor"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "nec sx-4 vector processor"]], "sel": 2}`
- Error: logical-form mismatch

## test:3902:1-27765443-2

- Question: Name the number of processors for october 2006 - january 2010
- Gold: `{"sel": 2, "conds": [[3, 0, "October 2006 - January 2010"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "October 2006 - January 2010"]], "sel": 2}`
- Error: logical-form mismatch

## test:3904:1-27781212-1

- Question: how many winnings does jeff gordon have?
- Gold: `{"sel": 3, "conds": [[1, 0, "Jeff Gordon"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "Jeff Gordon"]], "sel": 3}`
- Error: logical-form mismatch

## test:3913:1-27790959-1

- Question: What number in the season was "Burning Down the House"?
- Gold: `{"sel": 1, "conds": [[2, 0, "\"Burning Down the House\""]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Burning Down the House"]], "sel": 1}`
- Error: logical-form mismatch

## test:3916:1-27790959-1

- Question: How many million viewers watched "You Smell like Dinner"?
- Gold: `{"sel": 6, "conds": [[2, 0, "\"You Smell Like Dinner\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "You Smell Like Dinner"]], "sel": 6}`
- Error: logical-form mismatch

## test:3917:1-27834100-1

- Question: What is the episode number of "Dance Cards and Greeting Cards"?
- Gold: `{"sel": 0, "conds": [[2, 0, "\"Dance Cards and Greeting Cards\""]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "\"Dance Cards and Greeting Cards\""]], "sel": 1}`
- Error: logical-form mismatch

## test:3925:1-27846651-1

- Question: What episode in the series had 5.24 million viewers?
- Gold: `{"sel": 1, "conds": [[6, 0, "5.24"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "5.24"]], "sel": 0}`
- Error: logical-form mismatch

## test:3927:1-27846651-1

- Question: Who wrote "what you mean by home"?
- Gold: `{"sel": 4, "conds": [[2, 0, "\"What You Mean By Home\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "What You Mean By Home"]], "sel": 4}`
- Error: logical-form mismatch

## test:3988:1-28089666-1

- Question: What episode in the series is "teased"?
- Gold: `{"sel": 0, "conds": [[2, 0, "\"Teased\""]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Teased"]], "sel": 0}`
- Error: logical-form mismatch

## test:3993:1-28140588-1

- Question: Who is the director when the title is listed as "all guts, no glory"?
- Gold: `{"sel": 3, "conds": [[2, 0, "\"All Guts, No Glory\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "all guts, no glory"]], "sel": 3}`
- Error: logical-form mismatch

## test:3995:1-28140584-1

- Question: What number episode in the series was titled "Best Laid Plans"?
- Gold: `{"sel": 0, "conds": [[2, 0, "\"Best Laid Plans\""]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Best Laid Plans"]], "sel": 0}`
- Error: logical-form mismatch

## test:3996:1-2818164-5

- Question: What episode number in the series is "the drum major"?
- Gold: `{"sel": 0, "conds": [[2, 0, "\"The Drum Major\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "The Drum Major"]], "sel": 0}`
- Error: logical-form mismatch

## test:4067:1-28654454-5

- Question: What was miles's bmi att the reunion?
- Gold: `{"sel": 5, "conds": [[0, 0, "Miles"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Miles"]], "sel": 5}`
- Error: logical-form mismatch

## test:4086:1-28693349-2

- Question: How many points per game did Jack Williams score?
- Gold: `{"sel": 5, "conds": [[0, 0, "Jack Williams"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Jack Williams"]], "sel": 5}`
- Error: logical-form mismatch

## test:4104:1-28741-1

- Question: What are the numbers for GDP (nominal) per capita and USD (2012) of the area with Phnom Penh as capital?
- Gold: `{"sel": 5, "conds": [[7, 0, "Phnom Penh"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[7, 0, "Phnom Penh"]], "sel": 5}`
- Error: logical-form mismatch

## test:4123:1-28802165-1

- Question: How many acres is the townland of Maddenstown Middle?
- Gold: `{"sel": 1, "conds": [[0, 0, "Maddenstown Middle"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Maddenstown Middle"]], "sel": 1}`
- Error: logical-form mismatch

## test:4147:1-2889810-2

- Question: how many country has moto3/125cc with 15
- Gold: `{"sel": 0, "conds": [[4, 0, 15]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 0, 15]], "sel": 0}`
- Error: logical-form mismatch

## test:4157:1-28967275-3

- Question: When "the secret of deep stadium" is the episode title what is the lowest series number?
- Gold: `{"sel": 1, "conds": [[2, 0, "\"The Secret of Deep Stadium\""]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[2, 0, "the secret of deep stadium"]], "sel": 1}`
- Error: logical-form mismatch

## test:4167:1-29012710-1

- Question: what is the most number where cattle is 13000
- Gold: `{"sel": 0, "conds": [[2, 0, 13000]], "agg": 3}`
- Prediction: `{"agg": 1, "conds": [[2, 0, 13000]], "sel": 1}`
- Error: logical-form mismatch

## test:4168:1-29012710-1

- Question: what is the amount where the area is new brunswick
- Gold: `{"sel": 3, "conds": [[0, 0, "New Brunswick"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "new brunswick"]], "sel": 1}`
- Error: logical-form mismatch

## test:4169:1-29012710-1

- Question: what is the location where there are over 200 cattle businesses
- Gold: `{"sel": 0, "conds": [[1, 0, 200]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 1, 200]], "sel": 0}`
- Error: logical-form mismatch

## test:4172:1-29054902-1

- Question: How many millions of U.S viewers watched the episode titled "Miss Mystic Falls"?
- Gold: `{"sel": 6, "conds": [[1, 0, "\"Miss Mystic Falls\""]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "\"Miss Mystic Falls\""]], "sel": 6}`
- Error: logical-form mismatch

## test:4174:1-29054902-1

- Question: Who wrote the episode titled "There Goes the Neighborhood"? 
- Gold: `{"sel": 3, "conds": [[1, 0, "\"There Goes the Neighborhood\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "There Goes the Neighborhood"]], "sel": 3}`
- Error: logical-form mismatch

## test:4191:1-291768-1

- Question: which vessel area was called for on november 30, 1970
- Gold: `{"sel": 2, "conds": [[5, 0, "November 30, 1970"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "november 30, 1970"]], "sel": 0}`
- Error: logical-form mismatch

## test:4192:1-291768-1

- Question: what project was initially started before september 20, 1968
- Gold: `{"sel": 5, "conds": [[4, 0, "September 20, 1968"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 2, "september 20, 1968"]], "sel": 1}`
- Error: logical-form mismatch

## test:4193:1-291768-1

- Question: when was the first start date that actually began on august 6, 1969
- Gold: `{"sel": 4, "conds": [[5, 0, "August 6, 1969"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "august 6, 1969"]], "sel": 3}`
- Error: logical-form mismatch

## test:4198:1-29436007-1

- Question: How many episodes of the season had the title, "world's greatest dick"?
- Gold: `{"sel": 1, "conds": [[2, 0, "\"World's Greatest Dick\""]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "World's Greatest Dick"]], "sel": 1}`
- Error: logical-form mismatch

## test:4200:1-29436007-1

- Question: Who wrote "romeo & Juliet & dick"?
- Gold: `{"sel": 4, "conds": [[2, 0, "\"Romeo & Juliet & Dick\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Romeo & Juliet & Dick"]], "sel": 4}`
- Error: logical-form mismatch

## test:4212:1-29487895-2

- Question: What country is in the region of France?
- Gold: `{"sel": 3, "conds": [[0, 0, "France"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "France"]], "sel": 0}`
- Error: logical-form mismatch

## test:4218:1-29499399-2

- Question: Which money list ranks had a best finish of 2?
- Gold: `{"sel": 4, "conds": [[3, 0, "2"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "2"]], "sel": 4}`
- Error: logical-form mismatch

## test:4219:1-29499399-2

- Question: What is Jonathan Kaye's money list ranking?
- Gold: `{"sel": 4, "conds": [[0, 0, "Jonathan Kaye"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Jonathan Kaye"]], "sel": 4}`
- Error: logical-form mismatch

## test:4231:1-29615165-5

- Question: how many 20-39% are in pont-de-vivaux?
- Gold: `{"sel": 2, "conds": [[0, 0, "Pont-de-Vivaux"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Pont-de-Vivaux"]], "sel": 2}`
- Error: logical-form mismatch

## test:4234:1-29585196-1

- Question: What episode number in the season is "many happy returns"?
- Gold: `{"sel": 1, "conds": [[2, 0, "\"Many Happy Returns\""]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "many happy returns"]], "sel": 1}`
- Error: logical-form mismatch

## test:4235:1-29585196-1

- Question: How many episodes in the season were named "knight sting"?
- Gold: `{"sel": 1, "conds": [[2, 0, "\"Knight Sting\""]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "Knight Sting"]], "sel": 1}`
- Error: logical-form mismatch

## test:4238:1-29626583-1

- Question: how many pick# does the chivas usa  mls team have
- Gold: `{"sel": 0, "conds": [[1, 0, "Chivas USA"]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "Chivas USA"]], "sel": 0}`
- Error: logical-form mismatch

## test:4244:1-29747178-3

- Question: What number episode in the season was titled "Shattered"?
- Gold: `{"sel": 1, "conds": [[2, 0, "\"Shattered\""]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Shattered"]], "sel": 1}`
- Error: logical-form mismatch

## test:4253:1-29788320-2

- Question: How many editions did Club Q-base concept have ? 
- Gold: `{"sel": 4, "conds": [[0, 0, "Club Q-BASE"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Club Q-BASE"]], "sel": 4}`
- Error: logical-form mismatch

## test:4265:1-29871617-1

- Question: Which chromosomes have an unknown property?
- Gold: `{"sel": 0, "conds": [[4, 0, "Unknown"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "Unknown"]], "sel": 5}`
- Error: logical-form mismatch

## test:4269:1-30007505-1

- Question: Name the number of semifinalists for 19 rank
- Gold: `{"sel": 7, "conds": [[0, 0, 19]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 19]], "sel": 7}`
- Error: logical-form mismatch

## test:4303:1-30120559-1

- Question: Name the poor law union for area being 332
- Gold: `{"sel": 4, "conds": [[1, 0, 332]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, 332]], "sel": 4}`
- Error: logical-form mismatch

## test:4304:1-30121096-1

- Question: How many townlands are there for caheragh and is larger than 270 acres?
- Gold: `{"sel": 0, "conds": [[3, 0, "Caheragh"], [1, 0, 270]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "Caheragh"], [1, 1, 270]], "sel": 0}`
- Error: logical-form mismatch

## test:4394:2-10125431-14

- Question: What is total number of wins for England?
- Gold: `{"sel": 5, "conds": [[1, 0, "england"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "England"]], "sel": 2}`
- Error: logical-form mismatch

## test:4395:2-10125431-14

- Question: The Soviet Union has won more than 2 Silver, but how many Bronzes?
- Gold: `{"sel": 4, "conds": [[1, 0, "soviet union"], [3, 1, 2]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Soviet Union"], [3, 1, 2]], "sel": 4}`
- Error: logical-form mismatch

## test:4396:2-10107334-6

- Question: What are the election totals for David Cook who has 6,963 votes and 21.3 percentage?
- Gold: `{"sel": 2, "conds": [[3, 0, "david cook"], [4, 0, "6,963"], [5, 1, 21.3]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "David Cook"], [4, 0, 6963], [5, 0, 21.3]], "sel": 2}`
- Error: logical-form mismatch

## test:4414:2-10096494-5

- Question: What is the amount of assists for richmond kickers and points larger than 24
- Gold: `{"sel": 4, "conds": [[2, 0, "richmond kickers"], [5, 1, 24]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "richmond kickers"], [5, 1, 24]], "sel": 4}`
- Error: logical-form mismatch

## test:4437:2-10122032-1

- Question: How many gold medals on average were earned by Italy when they held the rank of 4?
- Gold: `{"sel": 2, "conds": [[1, 0, "italy"], [0, 1, 4]], "agg": 5}`
- Prediction: `{"agg": 5, "conds": [[1, 0, "Italy"], [0, 0, 4]], "sel": 2}`
- Error: logical-form mismatch

## test:4454:2-1006057-3

- Question: Which country is ranked number 2 and has less than 5 total medals?
- Gold: `{"sel": 3, "conds": [[0, 0, 2], [5, 2, 5]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 2], [5, 2, 5]], "sel": 1}`
- Error: logical-form mismatch

## test:4475:2-10089291-3

- Question: Tell me the MPEG-2 of yes and MPEG-1 of yes
- Gold: `{"sel": 5, "conds": [[1, 0, "yes"], [0, 0, "yes"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Yes"]], "sel": 1}`
- Error: logical-form mismatch

## test:4503:2-10776868-1

- Question: What was the attendance when the VFL played Lake Oval?
- Gold: `{"sel": 5, "conds": [[4, 0, "lake oval"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "lake oval"]], "sel": 5}`
- Error: logical-form mismatch

## test:4535:2-10706961-2

- Question: Who won for Forsythe Racing when Bobby Rahal had pole position?
- Gold: `{"sel": 0, "conds": [[4, 0, "forsythe racing"], [1, 0, "bobby rahal"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Bobby Rahal"], [4, 0, "Forsythe Racing"]], "sel": 3}`
- Error: logical-form mismatch

## test:4555:2-10775890-15

- Question: What day did the VFL pay MCG with attendance of 16,300?
- Gold: `{"sel": 6, "conds": [[5, 1, "16,300"], [4, 0, "mcg"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "MCG"], [5, 0, "16,300"]], "sel": 6}`
- Error: logical-form mismatch

## test:4556:2-10775890-15

- Question: What was the attendance when Fitzroy played as home team?
- Gold: `{"sel": 5, "conds": [[0, 0, "fitzroy"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Fitzroy"]], "sel": 5}`
- Error: logical-form mismatch

## test:4557:2-10775890-15

- Question: What was the attendance when Hawthorn played as home team?
- Gold: `{"sel": 5, "conds": [[0, 0, "hawthorn"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "hawthorn"]], "sel": 5}`
- Error: logical-form mismatch

## test:4560:2-10637245-1

- Question: Who used the Honda Engine for all the races?
- Gold: `{"sel": 0, "conds": [[2, 0, "honda"], [5, 0, "all"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Honda"], [5, 0, "All"]], "sel": 4}`
- Error: logical-form mismatch

## test:4564:2-10662806-1

- Question: Who won Silverstone in a round after 10?
- Gold: `{"sel": 1, "conds": [[0, 1, 10], [2, 0, "silverstone"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Silverstone"], [0, 1, 10]], "sel": 4}`
- Error: logical-form mismatch

## test:4597:2-10701045-12

- Question: When the Home team score was 8.15 (63), what is the total Crowd?
- Gold: `{"sel": 5, "conds": [[1, 0, "8.15 (63)"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "8.15 (63)"]], "sel": 5}`
- Error: logical-form mismatch

## test:4608:2-10672618-1

- Question: In what round was a defensive tackle drafted with an overall pick smaller than 149?
- Gold: `{"sel": 0, "conds": [[3, 0, "defensive tackle"], [1, 2, 149]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "defensive tackle"], [1, 2, 149]], "sel": 0}`
- Error: logical-form mismatch

## test:4612:2-10701914-11

- Question: How many attended the game with north melbourne as the away side?
- Gold: `{"sel": 5, "conds": [[2, 0, "melbourne"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "north melbourne"]], "sel": 5}`
- Error: logical-form mismatch

## test:4631:2-1054502-1

- Question: Which competition did Târlea come in 4th place, in 2003 at Budapest, Hungary?
- Gold: `{"sel": 1, "conds": [[3, 0, "4th"], [0, 1, 2003], [2, 0, "budapest, hungary"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "4th"], [0, 0, 2003], [2, 0, "Budapest, Hungary"]], "sel": 1}`
- Error: logical-form mismatch

## test:4657:2-10728418-3

- Question: Which building was built in 2015, has less than 40 floors and is larger than 509 feet?
- Gold: `{"sel": 2, "conds": [[5, 0, "2015"], [4, 2, 40], [3, 1, 509]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "2015"], [4, 2, 40], [3, 1, 509]], "sel": 0}`
- Error: logical-form mismatch

## test:4658:2-10728418-3

- Question: What is the highest floor for the building measuring 220 meters?
- Gold: `{"sel": 4, "conds": [[2, 1, 220]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[2, 0, 220]], "sel": 4}`
- Error: logical-form mismatch

## test:4701:2-1064022-2

- Question: What are the fewest losses for a player lower than 3, with wins fewer than 75%, 0 draws and 56 points?
- Gold: `{"sel": 1, "conds": [[0, 1, 3], [5, 2, 75], [2, 0, 0], [4, 0, 56]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[0, 2, 3], [5, 2, 75], [2, 0, 0], [4, 0, 56]], "sel": 1}`
- Error: logical-form mismatch

## test:4704:2-1064022-2

- Question: What is the smallest draws for a player larger than 2 with a 100% wins?
- Gold: `{"sel": 2, "conds": [[0, 1, 2], [5, 1, 100]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[0, 1, 2], [5, 0, 100]], "sel": 2}`
- Error: logical-form mismatch

## test:4712:2-10640687-2

- Question: What Away team scored 7.11 (53)?
- Gold: `{"sel": 0, "conds": [[3, 0, "7.11 (53)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "7.11 (53)"]], "sel": 2}`
- Error: logical-form mismatch

## test:4713:2-10640687-2

- Question: Which Home team scored 6.11 (47)?
- Gold: `{"sel": 2, "conds": [[1, 0, "6.11 (47)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "6.11 (47)"]], "sel": 0}`
- Error: logical-form mismatch

## test:4734:2-10577744-3

- Question: What is the highest ranked player who opposed Westmeath?
- Gold: `{"sel": 0, "conds": [[5, 0, "westmeath"]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "Westmeath"]], "sel": 1}`
- Error: logical-form mismatch

## test:4746:2-10746200-9

- Question: What was the score when geelong was the away team?
- Gold: `{"sel": 1, "conds": [[0, 0, "geelong"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "geelong"]], "sel": 3}`
- Error: logical-form mismatch

## test:4750:2-10640687-3

- Question: What was the attendance at the St Kilda home game?
- Gold: `{"sel": 5, "conds": [[0, 0, "st kilda"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "St Kilda"]], "sel": 5}`
- Error: logical-form mismatch

## test:4751:2-10640687-3

- Question: What was the attendance when the VFL played Junction Oval?
- Gold: `{"sel": 5, "conds": [[4, 0, "junction oval"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "junction oval"]], "sel": 5}`
- Error: logical-form mismatch

## test:4762:2-10773753-8

- Question: Who was the home team in the game played at arden street oval?
- Gold: `{"sel": 1, "conds": [[4, 0, "arden street oval"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "arden street oval"]], "sel": 0}`
- Error: logical-form mismatch

## test:4765:2-10774891-8

- Question: Which away team had a crowd larger than 22,000 at the Western Oval venue?
- Gold: `{"sel": 3, "conds": [[5, 1, "22,000"], [4, 0, "western oval"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 1, 22000], [4, 0, "Western Oval"]], "sel": 2}`
- Error: logical-form mismatch

## test:4798:2-10773753-11

- Question: What was the crowd numbers when the VFL played Victoria Park?
- Gold: `{"sel": 5, "conds": [[4, 0, "victoria park"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "victoria park"]], "sel": 5}`
- Error: logical-form mismatch

## test:4812:2-10701045-6

- Question: What was the crowd size at the match that had an away team score of 6.8 (44)?
- Gold: `{"sel": 5, "conds": [[3, 0, "6.8 (44)"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "6.8 (44)"]], "sel": 5}`
- Error: logical-form mismatch

## test:4826:2-10775890-4

- Question: Who played Fitzroy at their own home?
- Gold: `{"sel": 1, "conds": [[2, 0, "fitzroy"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Fitzroy"]], "sel": 0}`
- Error: logical-form mismatch

## test:4830:2-10773616-10

- Question: What is the away team's score when the home team scores 18.12 (120)?
- Gold: `{"sel": 2, "conds": [[1, 0, "18.12 (120)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "18.12 (120)"]], "sel": 3}`
- Error: logical-form mismatch

## test:4844:2-10775038-12

- Question: How many people saw the game that had a score of 15.10 (100)?
- Gold: `{"sel": 5, "conds": [[1, 0, "15.10 (100)"]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "15.10 (100)"]], "sel": 5}`
- Error: logical-form mismatch

## test:4861:2-10776868-12

- Question: Which crowd totals have away team scores of 16.6 (102)?
- Gold: `{"sel": 5, "conds": [[3, 0, "16.6 (102)"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "16.6 (102)"]], "sel": 5}`
- Error: logical-form mismatch

## test:4863:2-10648431-3

- Question: How many golds for Canada (12 total)?
- Gold: `{"sel": 2, "conds": [[5, 1, 12], [1, 0, "canada"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "Canada"], [5, 0, 12]], "sel": 2}`
- Error: logical-form mismatch

## test:4868:2-10660351-3

- Question: What team had less than 159 laps and a time or retired time of 4:00:30.7537 (retired - fire)?
- Gold: `{"sel": 0, "conds": [[2, 2, 159], [3, 0, "4:00:30.7537 (retired - fire)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 2, 159], [3, 0, "4:00:30.7537 (retired - fire)"]], "sel": 1}`
- Error: logical-form mismatch

## test:4881:2-10640687-18

- Question: What is the away team that features a home team of south melbourne?
- Gold: `{"sel": 3, "conds": [[0, 0, "south melbourne"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "south melbourne"]], "sel": 2}`
- Error: logical-form mismatch

## test:4884:2-10516034-1

- Question: What is the highest number of losses with 23 points and 22 plays?
- Gold: `{"sel": 5, "conds": [[2, 0, 23], [3, 1, 22]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[2, 0, 23], [3, 0, 22]], "sel": 5}`
- Error: logical-form mismatch

## test:4901:2-10710662-2

- Question: How many total points belong to the team with a goal difference of 8?
- Gold: `{"sel": 3, "conds": [[9, 0, 8]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[9, 0, 8]], "sel": 3}`
- Error: logical-form mismatch

## test:4903:2-1054817-1

- Question: How many teams played before 2008, had a K League Classic of runners-up, and a Manager of kim ho?
- Gold: `{"sel": 1, "conds": [[0, 2, 2008], [2, 0, "runners-up"], [5, 0, "kim ho"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 2, 2008], [2, 0, "Runners-up"], [5, 0, "Kim Ho"]], "sel": 1}`
- Error: logical-form mismatch

## test:4908:2-10775890-18

- Question: How many people watch an away team score 6.9 (45)?
- Gold: `{"sel": 5, "conds": [[3, 0, "6.9 (45)"]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "6.9 (45)"]], "sel": 5}`
- Error: logical-form mismatch

## test:4909:2-10775890-18

- Question: Who played a home team that scored 18.9 (117)?
- Gold: `{"sel": 3, "conds": [[1, 0, "18.9 (117)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "18.9 (117)"]], "sel": 2}`
- Error: logical-form mismatch

## test:4914:2-10766119-10

- Question: What was the attendance of the Hawthorn as the away team?
- Gold: `{"sel": 5, "conds": [[2, 0, "hawthorn"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "hawthorn"]], "sel": 5}`
- Error: logical-form mismatch

## test:4926:2-10756909-1

- Question: Which Lane had a 50m Split of 25.8?
- Gold: `{"sel": 0, "conds": [[3, 0, 25.8]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, 25.8]], "sel": 0}`
- Error: logical-form mismatch

## test:4931:2-10783853-16

- Question: What is the smallest crowd with fitzroy as the home team?
- Gold: `{"sel": 5, "conds": [[2, 0, "fitzroy"]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[0, 0, "fitzroy"]], "sel": 5}`
- Error: logical-form mismatch

## test:4932:2-10783853-16

- Question: What is the away team's score when the away side scores 8.7 (55)?
- Gold: `{"sel": 1, "conds": [[3, 0, "8.7 (55)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "8.7 (55)"]], "sel": 3}`
- Error: logical-form mismatch

## test:4948:2-13564702-4

- Question: What are the points for the Seven Sisters RFC club?
- Gold: `{"sel": 10, "conds": [[0, 0, "seven sisters rfc"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Seven Sisters RFC"]], "sel": 4}`
- Error: logical-form mismatch

## test:4950:2-13564702-4

- Question: How many tries had a losing bonus of 5, and were part of the Maesteg Celtic RFC club?
- Gold: `{"sel": 6, "conds": [[9, 0, "5"], [0, 0, "maesteg celtic rfc"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[9, 0, "5"], [0, 0, "Maesteg Celtic RFC"]], "sel": 6}`
- Error: logical-form mismatch

## test:4962:2-13599687-24

- Question: How many poles has a percentage of 22.08%?
- Gold: `{"sel": 3, "conds": [[4, 0, "22.08%"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "22.08%"]], "sel": 3}`
- Error: logical-form mismatch

## test:4964:2-15019672-21

- Question: How much Loss has an Avg/G larger than 129.2?
- Gold: `{"sel": 3, "conds": [[5, 1, 129.2]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 1, 129.2]], "sel": 3}`
- Error: logical-form mismatch

## test:4966:2-15019672-21

- Question: How much Avg/G has a Loss larger than 117, and a Name of opponents, and a Gain smaller than 2444?
- Gold: `{"sel": 5, "conds": [[3, 1, 117], [0, 0, "opponents"], [2, 2, 2444]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 1, 117], [0, 0, "opponents"], [2, 2, 2444]], "sel": 5}`
- Error: logical-form mismatch

## test:4967:2-15019672-21

- Question: How much Avg/G has a Long of 51, and a Loss of 333, and a Gain larger than 2013?
- Gold: `{"sel": 5, "conds": [[4, 0, 51], [3, 0, 333], [2, 1, 2013]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, 51], [3, 0, 333], [2, 1, 2013]], "sel": 5}`
- Error: logical-form mismatch

## test:4968:2-15019672-21

- Question: How much Avg/G has a Name of robert marve, and a Gain smaller than 236?
- Gold: `{"sel": 5, "conds": [[0, 0, "robert marve"], [2, 2, 236]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "robert marve"], [2, 2, 236]], "sel": 5}`
- Error: logical-form mismatch

## test:4971:2-151387-2

- Question: What was the score for an n/a location with the odds of p + 1?
- Gold: `{"sel": 2, "conds": [[4, 0, "n/a"], [3, 0, "p + 1"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "N/A"], [3, 0, "P + 1"]], "sel": 5}`
- Error: logical-form mismatch

## test:4979:2-14342210-2

- Question: How many points does Sweeley have, with less than 0 Field goals?
- Gold: `{"sel": 4, "conds": [[0, 0, "sweeley"], [3, 2, 0]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Sweeley"], [3, 2, 0]], "sel": 4}`
- Error: logical-form mismatch

## test:5003:2-14874370-1

- Question: What is the total number of Year that has an Album of Remixes?
- Gold: `{"sel": 4, "conds": [[2, 0, "remixes"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "RemixeS"]], "sel": 4}`
- Error: logical-form mismatch

## test:5020:2-14342480-15

- Question: How many touchdowns were made where field goals were less than 0?
- Gold: `{"sel": 1, "conds": [[3, 2, 0]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[3, 2, 0]], "sel": 1}`
- Error: logical-form mismatch

## test:5021:2-14342480-15

- Question: While Duncan Thompson played, how many points did he have where there were 0 field goals, 0 extra points, and more than 9 touchdowns?
- Gold: `{"sel": 4, "conds": [[3, 0, 0], [1, 1, 9], [2, 0, 0], [0, 0, "duncan thompson"]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Duncan Thompson"], [3, 0, 0], [2, 0, 0], [1, 1, 9]], "sel": 4}`
- Error: logical-form mismatch

## test:5022:2-14342480-15

- Question: When Herb Graver played, how many field goals were made when there were more than 50 points, less than 15 touchdowns, and more than 0 extra points?
- Gold: `{"sel": 3, "conds": [[4, 1, 50], [2, 1, 0], [0, 0, "herb graver"], [1, 2, 15]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Herb Graver"], [4, 1, 50], [1, 2, 15], [2, 1, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:5023:2-14342480-15

- Question: How many field goals were there, where the points where less than 45 and there were less than 15 touchdowns?
- Gold: `{"sel": 3, "conds": [[1, 2, 15], [4, 2, 45]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[4, 2, 45], [1, 2, 15]], "sel": 3}`
- Error: logical-form mismatch

## test:5028:2-14584481-1

- Question: How many races had 10.5 points?
- Gold: `{"sel": 3, "conds": [[8, 0, "10.5"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[8, 0, "10.5"]], "sel": 3}`
- Error: logical-form mismatch

## test:5036:2-14407512-3

- Question: Which 2nd (m) has a Rank larger than 1, and an Overall WC points (Rank) of 99 (8), and Points larger than 246.9?
- Gold: `{"sel": 4, "conds": [[0, 1, 1], [6, 0, "99 (8)"], [5, 1, 246.9]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 1, 1], [6, 0, "99 (8)"], [5, 1, 246.9]], "sel": 4}`
- Error: logical-form mismatch

## test:5037:2-14407512-3

- Question: How much Rank has a 1st (m) of 127?
- Gold: `{"sel": 0, "conds": [[3, 0, 127]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, 127]], "sel": 0}`
- Error: logical-form mismatch

## test:5039:2-14349165-2

- Question: How much Displacement (tons) has an Armament of 2 x -inch (mm), 16 x -inch (mm)?
- Gold: `{"sel": 2, "conds": [[3, 0, "2 x -inch (mm), 16 x -inch (mm)"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "2 x -inch (mm), 16 x -inch (mm)"]], "sel": 2}`
- Error: logical-form mismatch

## test:5053:2-14176339-4

- Question: What city had a score of 20 in aigburth after 1907?
- Gold: `{"sel": 3, "conds": [[4, 1, 1907], [0, 1, 20], [2, 0, "aigburth"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 20], [2, 0, "aigburth"], [4, 1, 1907]], "sel": 3}`
- Error: logical-form mismatch

## test:5067:2-15240821-3

- Question: What was the position for team corinthians with over 14 against?
- Gold: `{"sel": 0, "conds": [[1, 0, "corinthians"], [6, 1, 14]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Corinthians"], [6, 1, 14]], "sel": 0}`
- Error: logical-form mismatch

## test:5068:2-15240821-3

- Question: How many games played for team bangu with under 15 against, and over 9 points?
- Gold: `{"sel": 3, "conds": [[6, 2, 15], [1, 0, "bangu"], [2, 1, 9]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "Bangu"], [6, 2, 15], [2, 1, 9]], "sel": 3}`
- Error: logical-form mismatch

## test:5081:2-13742683-4

- Question: what's the grid with time +37.949?
- Gold: `{"sel": 4, "conds": [[3, 0, "+37.949"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "+37.949"]], "sel": 4}`
- Error: logical-form mismatch

## test:5091:2-14639984-3

- Question: Which Events have a Player of tom kite, and Earnings ($) smaller than 760,405?
- Gold: `{"sel": 4, "conds": [[1, 0, "tom kite"], [3, 2, "760,405"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "tom kite"], [3, 2, "760,405"]], "sel": 4}`
- Error: logical-form mismatch

## test:5117:2-15266104-2

- Question: Which Position has an Against of 5, and a Drawn larger than 0?
- Gold: `{"sel": 0, "conds": [[6, 0, 5], [4, 1, 0]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[6, 0, 5], [4, 1, 0]], "sel": 0}`
- Error: logical-form mismatch

## test:5120:2-13564637-3

- Question: what team lost the most points
- Gold: `{"sel": 3, "conds": [[10, 0, "points"]], "agg": 0}`
- Prediction: `{"agg": 1, "conds": [], "sel": 10}`
- Error: logical-form mismatch

## test:5150:2-14553873-1

- Question: How many wins are associated with 20 points and over 1 podium?
- Gold: `{"sel": 4, "conds": [[6, 0, 20], [5, 1, 1]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[6, 0, 20], [5, 1, 1]], "sel": 4}`
- Error: logical-form mismatch

## test:5157:2-13719531-1

- Question: What is the total grid number with laps that are larger than 27?
- Gold: `{"sel": 4, "conds": [[2, 1, 27]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[2, 1, 27]], "sel": 4}`
- Error: logical-form mismatch

## test:5168:2-14522314-2

- Question: Which Grid has a Driver of cristiano da matta, and Points smaller than 33?
- Gold: `{"sel": 4, "conds": [[0, 0, "cristiano da matta"], [5, 2, 33]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "cristiano da matta"], [5, 2, 33]], "sel": 4}`
- Error: logical-form mismatch

## test:5181:2-14050485-3

- Question: Sfax has a total ordered number of?
- Gold: `{"sel": 2, "conds": [[0, 0, "sfax"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Sfax"]], "sel": 2}`
- Error: logical-form mismatch

## test:5191:2-14611491-3

- Question: Tiger Woods has played less than 21 events and is what rank?
- Gold: `{"sel": 0, "conds": [[1, 0, "tiger woods"], [4, 2, 21]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "tiger woods"], [4, 2, 21]], "sel": 0}`
- Error: logical-form mismatch

## test:5210:2-15214004-3

- Question: How many picks did Mike Zaher have?
- Gold: `{"sel": 0, "conds": [[2, 0, "mike zaher"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "Mike Zaher"]], "sel": 0}`
- Error: logical-form mismatch

## test:5213:2-14083524-2

- Question: what day did the team go to toronto
- Gold: `{"sel": 0, "conds": [[1, 0, "toronto"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "toronto"]], "sel": 0}`
- Error: logical-form mismatch

## test:5214:2-14083524-2

- Question: what team visited chicago
- Gold: `{"sel": 2, "conds": [[1, 0, "chicago"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "chicago"]], "sel": 1}`
- Error: logical-form mismatch

## test:5215:2-14083524-2

- Question: what team played on october 8
- Gold: `{"sel": 3, "conds": [[0, 0, "october 8"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "october 8"]], "sel": 1}`
- Error: logical-form mismatch

## test:5241:2-1353887-1

- Question: Total points for a bs automotive entrant?
- Gold: `{"sel": 5, "conds": [[1, 0, "bs automotive"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "bs automotive"]], "sel": 5}`
- Error: logical-form mismatch

## test:5244:2-140465-4

- Question: How many Passengers that have an Airport in indonesia, denpasar?
- Gold: `{"sel": 2, "conds": [[1, 0, "indonesia, denpasar"]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "indonesia, denpasar"]], "sel": 2}`
- Error: logical-form mismatch

## test:5273:2-14027795-2

- Question: What is the number with the f position in Dallas, Texas?
- Gold: `{"sel": 1, "conds": [[2, 0, "f"], [5, 0, "dallas, texas"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "F"], [5, 0, "Dallas, Texas"]], "sel": 1}`
- Error: logical-form mismatch

## test:5285:2-14115168-5

- Question: Which Founded has a Club of tri-city storm and a Titles larger than 1?
- Gold: `{"sel": 4, "conds": [[0, 0, "tri-city storm"], [3, 1, 1]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "tri-city storm"], [3, 1, 1]], "sel": 4}`
- Error: logical-form mismatch

## test:5290:2-13648477-2

- Question: What grid has an average time of +22.505 and laps larger than 23?
- Gold: `{"sel": 4, "conds": [[3, 0, "+22.505"], [2, 1, 23]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "+22.505"], [2, 1, 23]], "sel": 4}`
- Error: logical-form mismatch

## test:5291:2-13648477-2

- Question: Which suzuki gsx-r1000 k7 has the highest time of retirement?
- Gold: `{"sel": 4, "conds": [[3, 0, "retirement"], [1, 0, "suzuki gsx-r1000 k7"]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[1, 0, "Suzuki GSX-R1000 K7"], [3, 0, "Retirement"]], "sel": 2}`
- Error: logical-form mismatch

## test:5297:2-14385890-3

- Question: How many TDs have a Car of 88 and an Avg smaller than 3?
- Gold: `{"sel": 4, "conds": [[1, 0, 88], [3, 2, 3]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[1, 0, 88], [3, 2, 3]], "sel": 4}`
- Error: logical-form mismatch

## test:5298:2-14385890-3

- Question: What is the amount of Avg that has Yards more 265 and a Car more 105?
- Gold: `{"sel": 3, "conds": [[2, 1, 265], [1, 1, 105]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 1, 265], [1, 1, 105]], "sel": 3}`
- Error: logical-form mismatch

## test:5312:2-15211468-2

- Question: What is the broadcast date for the episode titled, "From Hong Kong to Ulaanbaatar"?
- Gold: `{"sel": 2, "conds": [[1, 0, "\"from hong kong to ulaanbaatar\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "From Hong Kong to Ulaanbaatar"]], "sel": 2}`
- Error: logical-form mismatch

## test:5313:2-15211468-2

- Question: What is the broadcast date for the episode titled, "St. Petersburg to Tashkent"?
- Gold: `{"sel": 2, "conds": [[1, 0, "\"st. petersburg to tashkent\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "St. Petersburg to Tashkent"]], "sel": 2}`
- Error: logical-form mismatch

## test:5314:2-13810690-6

- Question: How many people attended the game on May 31?
- Gold: `{"sel": 4, "conds": [[0, 0, "may 31"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "May 31"]], "sel": 4}`
- Error: logical-form mismatch

## test:5315:2-13810690-6

- Question: How many people attended the game on May 10?
- Gold: `{"sel": 4, "conds": [[0, 0, "may 10"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "May 10"]], "sel": 4}`
- Error: logical-form mismatch

## test:5324:2-1431459-5

- Question: Which republican was first elected in 1886 in the district of ohio 17?
- Gold: `{"sel": 4, "conds": [[2, 0, "republican"], [3, 0, "1886"], [0, 0, "ohio 17"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Republican"], [3, 0, "1886"], [0, 0, "ohio 17"]], "sel": 1}`
- Error: logical-form mismatch

## test:5335:2-14196346-1

- Question: Which 8.23 g (127 gr) has a Bullet weight gram (grain) of 8x64mm s, and a 12.96 g (200 gr) smaller than 102.9?
- Gold: `{"sel": 1, "conds": [[0, 0, "8x64mm s"], [4, 2, 102.9]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "8x64mm S"], [4, 2, 102.9]], "sel": 1}`
- Error: logical-form mismatch

## test:5336:2-14196346-1

- Question: Which 9.72 g (150 gr) has a Bullet weight gram (grain) of .325 wsm, and an 8.23 g (127 gr) smaller than 108.7?
- Gold: `{"sel": 2, "conds": [[0, 0, ".325 wsm"], [1, 2, 108.7]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, ".325 WSM"], [1, 2, 108.7]], "sel": 2}`
- Error: logical-form mismatch

## test:5338:2-14196346-1

- Question: Which Case capacity (%) has a 9.72 g (150 gr) larger than 112.3?
- Gold: `{"sel": 6, "conds": [[2, 1, 112.3]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 1, 112.3]], "sel": 6}`
- Error: logical-form mismatch

## test:5340:2-13874304-2

- Question: What Goals with a Level of 5 or greater is the lowest?
- Gold: `{"sel": 5, "conds": [[1, 1, 5]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[1, 3, 5]], "sel": 5}`
- Error: operator 3 is not executable

## test:5348:2-1445467-1

- Question: What is the total capacity of venues that opened in 1999?
- Gold: `{"sel": 4, "conds": [[3, 0, "1999"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[3, 0, "1999"]], "sel": 4}`
- Error: logical-form mismatch

## test:5372:2-14342592-13

- Question: How many Extra Points were scored by the Player who had 5 Points and less than 1 Touchdowns?
- Gold: `{"sel": 2, "conds": [[4, 0, 5], [1, 2, 1]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[4, 0, 5], [1, 2, 1]], "sel": 2}`
- Error: logical-form mismatch

## test:5377:2-13741576-2

- Question: How many tries when 22 are played with 1 draw and a try bonus of 13?
- Gold: `{"sel": 7, "conds": [[1, 0, "22"], [2, 0, "1"], [8, 0, "13"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "22"], [2, 0, "1"], [8, 0, "13"]], "sel": 6}`
- Error: logical-form mismatch

## test:5378:2-13741576-2

- Question: How many points were scored against with a losing bonus of 1 for Blaenavon RFC?
- Gold: `{"sel": 5, "conds": [[9, 0, "1"], [0, 0, "blaenavon rfc"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[9, 0, "1"], [0, 0, "Blaenavon RFC"]], "sel": 5}`
- Error: logical-form mismatch

## test:5385:2-14344289-5

- Question: Which Points have an Opponent of calgary flames, and a January larger than 22?
- Gold: `{"sel": 5, "conds": [[2, 0, "calgary flames"], [1, 1, 22]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "calgary flames"], [1, 1, 22]], "sel": 5}`
- Error: logical-form mismatch

## test:5390:2-14290390-3

- Question: Which Attendance has an Opponent of pittsburgh pirates, and a Date of may 5?
- Gold: `{"sel": 4, "conds": [[1, 0, "pittsburgh pirates"], [0, 0, "may 5"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "pittsburgh pirates"], [0, 0, "may 5"]], "sel": 4}`
- Error: logical-form mismatch

## test:5428:2-14344570-4

- Question: Which December has a Record of 21–8–4, and a Game larger than 33?
- Gold: `{"sel": 1, "conds": [[4, 0, "21–8–4"], [0, 1, 33]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "21–8–4"], [0, 1, 33]], "sel": 1}`
- Error: logical-form mismatch

## test:5432:2-14611491-1

- Question: What is the date of the sprint international tournament where the first prize was 216,000 dollars?
- Gold: `{"sel": 0, "conds": [[5, 1, "216,000"], [1, 0, "sprint international"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Sprint International"], [5, 0, "216,000"]], "sel": 0}`
- Error: logical-form mismatch

## test:5433:2-14617448-3

- Question: What is the total TD's of the strongest storm William that has a total TC's smaller than 2?
- Gold: `{"sel": 1, "conds": [[4, 0, "william"], [2, 2, 2]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[4, 0, "william"], [2, 2, 2]], "sel": 1}`
- Error: logical-form mismatch

## test:5439:2-1370559-1

- Question: What is the shot % with a 44+ Ends Lost, skip Cathy King, and smaller than 13 Black Ends?
- Gold: `{"sel": 6, "conds": [[3, 1, 44], [1, 0, "cathy king"], [4, 2, 13]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[3, 1, 44], [1, 0, "Cathy King"], [4, 2, 13]], "sel": 6}`
- Error: logical-form mismatch

## test:5443:2-14265680-2

- Question: Which church had a Split off/Continuation in 1836?
- Gold: `{"sel": 3, "conds": [[2, 0, "1836"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "1836"]], "sel": 0}`
- Error: logical-form mismatch

## test:5473:2-14139408-1

- Question: Which Poles has a Wins larger than 0, and a Podiums smaller than 17?
- Gold: `{"sel": 4, "conds": [[2, 1, 0], [3, 2, 17], [5, 0, 0]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 1, 0], [3, 2, 17]], "sel": 4}`
- Error: logical-form mismatch

## test:5474:2-14139408-1

- Question: which Poles has a Fastest Laps of 0, and a Races of 17, and a Wins larger than 0, and a Podiums smaller than 2?
- Gold: `{"sel": 4, "conds": [[5, 0, 0], [1, 0, 17], [2, 1, 0], [3, 2, 2]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[5, 0, 0], [1, 0, 17], [2, 1, 0], [3, 2, 2]], "sel": 4}`
- Error: logical-form mismatch

## test:5475:2-14139408-1

- Question: How many Fastest Laps have  Poles of 4, and Races larger than 178?
- Gold: `{"sel": 5, "conds": [[4, 0, 4], [1, 1, 178]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[4, 0, 4], [1, 1, 178]], "sel": 5}`
- Error: logical-form mismatch

## test:5476:2-14139408-1

- Question: Which the Fastest Lap has a Season of 2009 and Poles smaller than 0?
- Gold: `{"sel": 5, "conds": [[0, 0, "2009"], [4, 2, 0]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "2009"], [4, 2, 0]], "sel": 5}`
- Error: logical-form mismatch

## test:5477:2-14139408-1

- Question: Which the Fastest Laps that have  Poles of 0, and a Season of 2002, and a Podiums smaller than 0?
- Gold: `{"sel": 5, "conds": [[4, 0, 0], [0, 0, "2002"], [3, 2, 0]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 0, 0], [0, 0, "2002"], [3, 2, 0]], "sel": 5}`
- Error: logical-form mismatch

## test:5484:2-14743082-1

- Question: What is the year of most recent appearance of the Suncoast sound, who had more than 7 finals appearances?
- Gold: `{"sel": 3, "conds": [[0, 0, "suncoast sound"], [1, 1, 7]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Suncoast sound"], [1, 1, 7]], "sel": 3}`
- Error: logical-form mismatch

## test:5485:2-14743082-1

- Question: What is the year of the first appearance of the Black Knights, who had less than 1 finals appearances?
- Gold: `{"sel": 2, "conds": [[0, 0, "black knights"], [1, 2, 1]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Black Knights"], [1, 2, 1]], "sel": 2}`
- Error: logical-form mismatch

## test:5486:2-15198842-33

- Question: What is the Pick # of the player with an Overall less than 203 from West Virginia?
- Gold: `{"sel": 1, "conds": [[5, 0, "west virginia"], [2, 2, 203]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 2, 203], [5, 0, "West Virginia"]], "sel": 1}`
- Error: logical-form mismatch

## test:5487:2-15198842-33

- Question: In what Round was the draft pick from Florida with an Overall less than 166?
- Gold: `{"sel": 0, "conds": [[5, 0, "florida"], [2, 2, 166]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "Florida"], [2, 2, 166]], "sel": 0}`
- Error: logical-form mismatch

## test:5506:2-14837173-3

- Question: What is the number in total of silver with a gold smaller than 0?
- Gold: `{"sel": 3, "conds": [[2, 2, 0]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[2, 2, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:5515:2-15124443-1

- Question: What was the total attendance with a result of W 31-21 before week 9?
- Gold: `{"sel": 4, "conds": [[3, 0, "w 31-21"], [0, 2, 9]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[3, 0, "W 31-21"], [0, 2, 9]], "sel": 4}`
- Error: logical-form mismatch

## test:5519:2-13581632-2

- Question: what game was in chicago
- Gold: `{"sel": 4, "conds": [[3, 0, "chicago"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "chicago"]], "sel": 2}`
- Error: logical-form mismatch

## test:5527:2-13909382-5

- Question: What is the number in January for Philadelphia Flyers as opponents?
- Gold: `{"sel": 1, "conds": [[2, 0, "philadelphia flyers"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Philadelphia Flyers"]], "sel": 1}`
- Error: logical-form mismatch

## test:5531:2-14954377-5

- Question: How many copies of scouting for girls were sold?
- Gold: `{"sel": 3, "conds": [[1, 0, "scouting for girls"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "scouting for girls"]], "sel": 3}`
- Error: logical-form mismatch

## test:5532:2-14954377-5

- Question: What was the position for albums made by elbow with under 424,000 sales?
- Gold: `{"sel": 0, "conds": [[3, 2, "424,000"], [2, 0, "elbow"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "elbow"], [3, 2, "424,000"]], "sel": 0}`
- Error: logical-form mismatch

## test:5555:2-14546539-2

- Question: When did the Indians play a game with 15,105 people in attendance?
- Gold: `{"sel": 0, "conds": [[4, 0, "15,105"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Indians"], [4, 0, "15,105"]], "sel": 0}`
- Error: logical-form mismatch

## test:5563:2-13658-1

- Question: Which Total has a Hereditary peer of –, and a Lords spiritual of –, and a Life peers of 2, and an Affiliation of plaid cymru?
- Gold: `{"sel": 4, "conds": [[2, 0, "–"], [3, 0, "–"], [1, 0, "2"], [0, 0, "plaid cymru"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "–"], [3, 0, "–"], [1, 0, "2"], [0, 0, "plaid cymru"]], "sel": 4}`
- Error: logical-form mismatch

## test:5566:2-14518594-1

- Question: Which Works number has a Number larger than 807, and a Type of 0-6-0, and a Date of 1920?
- Gold: `{"sel": 4, "conds": [[0, 1, 807], [2, 0, "0-6-0"], [3, 0, 1920]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 1, 807], [2, 0, "0-6-0"], [3, 0, 1920]], "sel": 4}`
- Error: logical-form mismatch

## test:5571:2-1453282-1

- Question: How many votes were there on November 10?
- Gold: `{"sel": 4, "conds": [[1, 0, "november 10"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "November 10"]], "sel": 4}`
- Error: logical-form mismatch

## test:5579:2-13986492-12

- Question: How many people enrolled a the school with an IHSAA Class of a, and the trojans as their mascot?
- Gold: `{"sel": 3, "conds": [[4, 0, "a"], [2, 0, "trojans"]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "a"], [2, 0, "trojans"]], "sel": 3}`
- Error: logical-form mismatch

## test:5597:2-14056076-6

- Question: What is the February number of the game played against the St. Louis Blues with a game number less than 58?
- Gold: `{"sel": 1, "conds": [[2, 0, "st. louis blues"], [0, 2, 58]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "St. Louis Blues"], [0, 2, 58]], "sel": 1}`
- Error: logical-form mismatch

## test:5599:2-14056076-6

- Question: What is the February number of the game with the Vancouver Canucks as the opponent and a game number greater than 55?
- Gold: `{"sel": 1, "conds": [[2, 0, "vancouver canucks"], [0, 1, 55]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Vancouver Canucks"], [0, 1, 55]], "sel": 1}`
- Error: logical-form mismatch

## test:5601:2-14827502-4

- Question: what team scored 17
- Gold: `{"sel": 1, "conds": [[0, 0, 17]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 17]], "sel": 2}`
- Error: logical-form mismatch

## test:5640:2-15194788-2

- Question: Which stage corresponds to Banesto and Tony Rominger?
- Gold: `{"sel": 0, "conds": [[5, 0, "banesto"], [3, 0, "tony rominger"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "Banesto"], [1, 0, "Tony Rominger"]], "sel": 0}`
- Error: logical-form mismatch

## test:5642:2-151199-6

- Question: Frequency (MHz) that has a Type of primary, and a Call letters of ktbb-fm has what total number?
- Gold: `{"sel": 0, "conds": [[3, 0, "primary"], [1, 0, "ktbb-fm"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[3, 0, "primary"], [1, 0, "ktbb-fm"]], "sel": 0}`
- Error: logical-form mismatch

## test:5655:2-144915-1

- Question: Who is the voice actor of the character with the Japanese voice actor Yoku Shioya?
- Gold: `{"sel": 12, "conds": [[9, 0, "yoku shioya"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[9, 0, "yoku shioya"]], "sel": 10}`
- Error: logical-form mismatch

## test:5689:2-1419115-1

- Question: When the population is greater than 146,445 in the county of Carroll, what is the number of households?
- Gold: `{"sel": 5, "conds": [[4, 1, "146,445"], [0, 0, "carroll"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[4, 1, "146,445"], [0, 0, "Carroll"]], "sel": 5}`
- Error: logical-form mismatch

## test:5694:2-14650162-2

- Question: which week had an attendance of 53,677?
- Gold: `{"sel": 0, "conds": [[5, 0, "53,677"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "53,677"]], "sel": 0}`
- Error: logical-form mismatch

## test:5717:2-14366878-3

- Question: How many losses have a year later than 2001?
- Gold: `{"sel": 3, "conds": [[0, 1, 2001]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 1, 2001]], "sel": 3}`
- Error: logical-form mismatch

## test:5725:2-14335332-3

- Question: How many points have pittsburgh as the visitor, and philadelphia as the home?
- Gold: `{"sel": 5, "conds": [[1, 0, "pittsburgh"], [3, 0, "philadelphia"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "pittsburgh"], [3, 0, "philadelphia"]], "sel": 5}`
- Error: logical-form mismatch

## test:5732:2-14819302-3

- Question: Before 1981, how many Points did Team Suzuki have with less than 0 Wins?
- Gold: `{"sel": 4, "conds": [[2, 0, "suzuki"], [0, 2, 1981], [5, 2, 0]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 2, 1981], [2, 0, "Suzuki"], [5, 2, 0]], "sel": 4}`
- Error: logical-form mismatch

## test:5733:2-14819302-3

- Question: After 1986, how many Wins did Lucky Strike Yamaha Team with less than 6 Points have?
- Gold: `{"sel": 5, "conds": [[0, 1, 1986], [2, 0, "lucky strike yamaha"], [4, 2, 6]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[0, 1, 1986], [2, 0, "Lucky Strike Yamaha"], [4, 2, 6]], "sel": 5}`
- Error: logical-form mismatch

## test:5734:2-14819302-3

- Question: In what Year did the RG500 Machine have more than 17 Points?
- Gold: `{"sel": 0, "conds": [[3, 0, "rg500"], [4, 1, 17]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "RG500"], [4, 1, 17]], "sel": 0}`
- Error: logical-form mismatch

## test:5736:2-14106667-6

- Question: How many points did the Flyers have against the New York Islanders with a February bigger than 12, and a game smaller than 60?
- Gold: `{"sel": 5, "conds": [[1, 1, 12], [0, 2, 60], [2, 0, "new york islanders"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "New York Islanders"], [1, 1, 12], [0, 2, 60]], "sel": 5}`
- Error: logical-form mismatch

## test:5764:2-15020951-1

- Question: Which Season has a Level of tier 2 and a Position of 1st?
- Gold: `{"sel": 0, "conds": [[1, 0, "tier 2"], [4, 0, "1st"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "tier 2"], [4, 0, "1st"]], "sel": 0}`
- Error: logical-form mismatch

## test:5767:2-1458587-1

- Question: How many people have a Median household income of $37,759?
- Gold: `{"sel": 4, "conds": [[2, 0, "$37,759"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "$37,759"]], "sel": 4}`
- Error: logical-form mismatch

## test:5768:2-15123167-2

- Question: What week had an Attendance smaller than 21,097?
- Gold: `{"sel": 0, "conds": [[4, 2, "21,097"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 2, 21097]], "sel": 0}`
- Error: logical-form mismatch

## test:5769:2-15123167-2

- Question: What Week had an Attendance smaller than 22,333?
- Gold: `{"sel": 0, "conds": [[4, 2, "22,333"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 2, 22333]], "sel": 0}`
- Error: logical-form mismatch

## test:5771:2-15124959-1

- Question: Quotient of 97 350,333 has how many votes?
- Gold: `{"sel": 2, "conds": [[3, 0, "97 350,333"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "97 350,333"]], "sel": 2}`
- Error: logical-form mismatch

## test:5810:2-13975482-1

- Question: What is the MHZ frequency in carmel, california with an ERP W over 10?
- Gold: `{"sel": 1, "conds": [[2, 0, "carmel, california"], [3, 1, 10]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Carmel, California"], [3, 1, 10]], "sel": 1}`
- Error: logical-form mismatch

## test:5814:2-15008664-15

- Question: Which Yards have an avg of 11.8, and a Player of brent celek, and a Long larger than 44?
- Gold: `{"sel": 2, "conds": [[3, 0, 11.8], [0, 0, "brent celek"], [4, 1, 44]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[3, 0, 11.8], [0, 0, "brent celek"], [4, 1, 44]], "sel": 2}`
- Error: logical-form mismatch

## test:5822:2-14342592-5

- Question: How many points does Tom Hammond have if he has more than 12 points?
- Gold: `{"sel": 4, "conds": [[0, 0, "tom hammond"], [2, 1, 12]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Tom Hammond"], [4, 1, 12]], "sel": 4}`
- Error: logical-form mismatch

## test:5870:2-13847695-3

- Question: What year was Incumbent Ed Towns elected with a district smaller than 10?
- Gold: `{"sel": 3, "conds": [[1, 0, "ed towns"], [0, 2, 10]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Ed Towns"], [0, 2, 10]], "sel": 3}`
- Error: logical-form mismatch

## test:5885:2-152750-1

- Question: Which area 2006 km² has an area 1996 km² of 26.39, and a pop 2006 smaller than 18,610?
- Gold: `{"sel": 2, "conds": [[1, 0, 26.39], [5, 2, "18,610"]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[1, 0, 26.39], [5, 2, "18,610"]], "sel": 2}`
- Error: logical-form mismatch

## test:5886:2-152750-1

- Question: Which area 2006 km² has a city of sopot, and an area 1996 km² smaller than 17.31?
- Gold: `{"sel": 2, "conds": [[0, 0, "sopot"], [1, 2, 17.31]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Sopot"], [1, 2, 17.31]], "sel": 2}`
- Error: logical-form mismatch

## test:5887:2-152750-1

- Question: Which area 1996 km² has a pop 1999 of 17,510, and an area 2006 km² larger than 30?
- Gold: `{"sel": 1, "conds": [[3, 0, "17,510"], [2, 1, 30]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "17,510"], [2, 1, 30]], "sel": 1}`
- Error: logical-form mismatch

## test:5895:2-15256675-3

- Question: What is the number of Silver medals with 2 Bronze and 0 Gold?
- Gold: `{"sel": 3, "conds": [[4, 0, 2], [2, 2, 0]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, 2], [2, 0, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:5919:2-15268424-3

- Question: How many wins in OT are associated with a W(GWS)* of 0, a Season of 2009–10, and a L(OT) less than 0?
- Gold: `{"sel": 1, "conds": [[2, 0, "0"], [0, 0, "2009–10"], [4, 2, 0]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "0"], [0, 0, "2009–10"], [4, 2, 0]], "sel": 1}`
- Error: logical-form mismatch

## test:5920:2-15268424-3

- Question: How many OT wins associated with a L(GWS)* of 3, and a L(OT) larger than 1?
- Gold: `{"sel": 1, "conds": [[3, 0, "3"], [4, 1, 1]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "3"], [4, 1, 1]], "sel": 1}`
- Error: logical-form mismatch

## test:5939:2-15016356-3

- Question: What number did Moño Negro peak at before 1996?
- Gold: `{"sel": 3, "conds": [[2, 0, "moño negro"], [0, 2, 1996]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Moño Negro"], [0, 2, 1996]], "sel": 3}`
- Error: logical-form mismatch

## test:5940:2-15016356-3

- Question: How many weeks was the track Abrazame on the Billboard Latin Pop airplay before 1997?
- Gold: `{"sel": 4, "conds": [[2, 0, "abrazame"], [1, 0, "billboard latin pop airplay"], [0, 2, 1997]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "Abrazame"], [1, 0, "Billboard Latin Pop airplay"], [0, 2, 1997]], "sel": 4}`
- Error: logical-form mismatch

## test:5952:2-14856478-2

- Question: Who created One Night in Lisbon in 1941?
- Gold: `{"sel": 3, "conds": [[2, 0, "1941"], [1, 0, "one night in lisbon"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "One Night in Lisbon"], [2, 0, "1941"]], "sel": 4}`
- Error: logical-form mismatch

## test:5955:2-14946156-1

- Question: How much Draw has a Televote larger than 18, and an Artist of elizabeth anastasiou, and a Jury larger than 4?
- Gold: `{"sel": 0, "conds": [[4, 1, 18], [1, 0, "elizabeth anastasiou"], [3, 1, 4]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 1, 18], [1, 0, "elizabeth anastasiou"], [3, 1, 4]], "sel": 0}`
- Error: logical-form mismatch

## test:5964:2-15041768-1

- Question: How many years had budgets of $39 million?
- Gold: `{"sel": 1, "conds": [[3, 0, "$39 million"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "$39 million"]], "sel": 1}`
- Error: logical-form mismatch

## test:5973:2-15062099-1

- Question: What is the capacity for the stadium of kadrioru stadium and a current manager of sergei ratnikov?
- Gold: `{"sel": 3, "conds": [[2, 0, "kadrioru stadium"], [4, 0, "sergei ratnikov"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "kadrioru stadium"], [4, 0, "sergei ratnikov"]], "sel": 3}`
- Error: logical-form mismatch

## test:5981:2-1508381-1

- Question: What is NK Rijeka's away score in Round 2?
- Gold: `{"sel": 3, "conds": [[0, 2, 2], [1, 0, "nk rijeka"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "NK Rijeka"], [0, 0, 2]], "sel": 3}`
- Error: logical-form mismatch

## test:5989:2-1524633-6

- Question: How many Total matches have a Year of career, and a Points won larger than 25?
- Gold: `{"sel": 1, "conds": [[0, 0, "career"], [4, 1, 25]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Career"], [4, 1, 25]], "sel": 1}`
- Error: logical-form mismatch

## test:6006:2-13669614-12

- Question: Which team opposed the Milwaukee Braves?
- Gold: `{"sel": 3, "conds": [[1, 0, "milwaukee braves"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Milwaukee Braves"]], "sel": 1}`
- Error: logical-form mismatch

## test:6009:2-1520730-5

- Question: How man cuts were there of players who had 0 wins but had 1 player in the top 25 with more than 4 events?
- Gold: `{"sel": 6, "conds": [[1, 0, 0], [4, 0, 1], [5, 1, 4]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, 0], [4, 0, 1], [5, 1, 4]], "sel": 6}`
- Error: logical-form mismatch

## test:6038:2-14098262-2

- Question: what pitcher scored 4
- Gold: `{"sel": 3, "conds": [[4, 0, "4"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "4"]], "sel": 2}`
- Error: logical-form mismatch

## test:6039:2-1473078-6

- Question: What was the rank for karen frohner with under 1266 points?
- Gold: `{"sel": 0, "conds": [[1, 0, "karen frohner"], [3, 2, 1266]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Karen Frohner"], [3, 2, 1266]], "sel": 0}`
- Error: logical-form mismatch

## test:6041:2-1399716-2

- Question: What is the number of Apps for Internazionale Club of Brazil?
- Gold: `{"sel": 3, "conds": [[0, 0, "brazil"], [1, 0, "internazionale"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Internazionale"], [0, 0, "Brazil"]], "sel": 3}`
- Error: logical-form mismatch

## test:6045:2-14888584-4

- Question: What is the number of years that Kim was nominated at the Sitges Film Festival?
- Gold: `{"sel": 0, "conds": [[1, 0, "sitges film festival"]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "Sitges Film Festival"], [4, 0, "Nominated"]], "sel": 0}`
- Error: logical-form mismatch

## test:6047:2-14888584-4

- Question: Which group nominated Kim in years before 2010 for Thirst?
- Gold: `{"sel": 1, "conds": [[0, 2, 2010], [3, 0, "thirst"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 2, 2010], [3, 0, "Thirst"], [4, 0, "Nominated"]], "sel": 1}`
- Error: logical-form mismatch

## test:6048:2-14888584-4

- Question: What is the highest year that Kim was nominated for Over the Rainbow?
- Gold: `{"sel": 0, "conds": [[3, 0, "over the rainbow"]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[3, 0, "Over the Rainbow"], [4, 0, "Nominated"]], "sel": 0}`
- Error: logical-form mismatch

## test:6075:2-13884212-1

- Question: How many Attendance in a match which scores  0:0 - 4:1 (pen)
- Gold: `{"sel": 4, "conds": [[3, 0, "0:0 - 4:1 (pen)"]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "0:0 - 4:1 (pen)"]], "sel": 4}`
- Error: logical-form mismatch

## test:6086:2-1512659-6

- Question: In the tournament that has 15 events, and less than 6 top-25's, how many top-5's did he have?
- Gold: `{"sel": 2, "conds": [[5, 0, 15], [4, 2, 6]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[5, 0, 15], [4, 2, 6]], "sel": 2}`
- Error: logical-form mismatch

## test:6087:2-1512659-6

- Question: In the tournament that had 3 Top-10's, and less than 15 events, how many Top-5's did the player have?
- Gold: `{"sel": 2, "conds": [[3, 0, 3], [5, 2, 15]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[3, 0, 3], [5, 2, 15]], "sel": 2}`
- Error: logical-form mismatch

## test:6088:2-1512659-6

- Question: How many wins were in the Masters Tournament with less than 15 events?
- Gold: `{"sel": 1, "conds": [[0, 0, "masters tournament"], [5, 2, 15]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Masters Tournament"], [5, 2, 15]], "sel": 1}`
- Error: logical-form mismatch

## test:6089:2-1512659-6

- Question: In the tournament with more than 6 top-25's and less than 13 cuts made, how many wins were there?
- Gold: `{"sel": 1, "conds": [[4, 1, 6], [6, 2, 13]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 1, 6], [6, 2, 13]], "sel": 1}`
- Error: logical-form mismatch

## test:6092:2-13849334-2

- Question: Which duchess was born on 9 october 1574?
- Gold: `{"sel": 3, "conds": [[2, 0, "9 october 1574"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "9 october 1574"]], "sel": 0}`
- Error: logical-form mismatch

## test:6101:2-1355180-1

- Question: How many people attended the 3rd round Emperor's cup with a TMS larger than 12?
- Gold: `{"sel": 4, "conds": [[5, 0, "3rd round"], [2, 1, 12]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[5, 0, "3rd Round"], [2, 1, 12]], "sel": 4}`
- Error: logical-form mismatch

## test:6128:2-14155268-3

- Question: Who was born on 10 May 1788 that ceased to be queen?
- Gold: `{"sel": 4, "conds": [[1, 0, "10 may 1788"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "10 May 1788"]], "sel": 0}`
- Error: logical-form mismatch

## test:6132:2-14269540-4

- Question: Which team has the record of 11-6?
- Gold: `{"sel": 3, "conds": [[5, 0, "11-6"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "11-6"]], "sel": 1}`
- Error: logical-form mismatch

## test:6157:2-14203256-1

- Question: How many Watts has a Class of a, and a Frequency of 91.5 fm, and a City of license of elkhart, kansas?
- Gold: `{"sel": 3, "conds": [[4, 0, "a"], [1, 0, "91.5 fm"], [2, 0, "elkhart, kansas"]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "a"], [1, 0, "91.5 fm"], [2, 0, "elkhart, kansas"]], "sel": 3}`
- Error: logical-form mismatch

## test:6175:2-15028555-1

- Question: What is the overall pick number that Derrick Harvey was when he was picked in a round after round 1?
- Gold: `{"sel": 2, "conds": [[3, 0, "derrick harvey"], [0, 1, 1]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Derrick Harvey"], [0, 1, 1]], "sel": 2}`
- Error: logical-form mismatch

## test:6181:2-14481629-1

- Question: What is the total number of Serious Bodily Injuries, that has Homicides less than 84?
- Gold: `{"sel": 3, "conds": [[2, 2, 84]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[2, 2, 84]], "sel": 3}`
- Error: logical-form mismatch

## test:6186:2-13880730-8

- Question: What was the Attendance during the Tamworth Away game?
- Gold: `{"sel": 4, "conds": [[3, 0, "tamworth"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Tamworth"]], "sel": 4}`
- Error: logical-form mismatch

## test:6187:2-14611466-1

- Question: Which 1st prize ($) has a Winner of scott simpson (7)?
- Gold: `{"sel": 5, "conds": [[3, 0, "scott simpson (7)"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "scott simpson (7)"]], "sel": 5}`
- Error: logical-form mismatch

## test:6196:2-14094649-22

- Question: Where is the company headquarted that has a Market value ( USD million) larger than 146,139, a Rank above 3, and a Primary industry of oil and gas?
- Gold: `{"sel": 2, "conds": [[4, 1, "146,139"], [0, 2, 3], [3, 0, "oil and gas"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 1, "146,139"], [0, 1, 3], [3, 0, "oil and gas"]], "sel": 2}`
- Error: logical-form mismatch

## test:6214:2-15213262-7

- Question: What is the date of the away venue with an opponent of wightlink raiders with an attendance larger than 375?
- Gold: `{"sel": 0, "conds": [[2, 0, "away"], [1, 0, "wightlink raiders"], [4, 1, 375]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "away"], [1, 0, "wightlink raiders"], [4, 1, 375]], "sel": 0}`
- Error: logical-form mismatch

## test:6246:2-14962316-9

- Question: what is the runner-up for the intercontinental cup
- Gold: `{"sel": 6, "conds": [[2, 0, "runner-up"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "runner-up"]], "sel": 0}`
- Error: logical-form mismatch

## test:6268:2-1353450-3

- Question: What is the total number of Laps that's got a Year less than 1987?
- Gold: `{"sel": 5, "conds": [[0, 2, 1987]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 2, 1987]], "sel": 5}`
- Error: logical-form mismatch

## test:6273:2-13564702-2

- Question: What is listed for Points for that has a Club of Club?
- Gold: `{"sel": 4, "conds": [[0, 0, "club"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Club"]], "sel": 10}`
- Error: logical-form mismatch

## test:6291:2-14202514-2

- Question: When was the earliest that New England Patriots played?
- Gold: `{"sel": 0, "conds": [[2, 0, "new england patriots"]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[2, 0, "New England Patriots"]], "sel": 1}`
- Error: logical-form mismatch

## test:6295:2-1436501-1

- Question: Which Match has Runs of 100, and a Year larger than 1994?
- Gold: `{"sel": 1, "conds": [[0, 0, 100], [4, 1, 1994]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 100], [4, 1, 1994]], "sel": 1}`
- Error: logical-form mismatch

## test:6299:2-13744010-2

- Question: What is the average number of silvers for teams ranked 5 with 0 bronze?
- Gold: `{"sel": 3, "conds": [[0, 0, "5"], [4, 2, 0]], "agg": 5}`
- Prediction: `{"agg": 5, "conds": [[0, 0, "5"], [4, 0, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:6308:2-15262161-1

- Question: What is the area (km²) of Nairnshire county, which has a population less than 11,050?
- Gold: `{"sel": 2, "conds": [[0, 0, "nairnshire"], [3, 2, "11,050"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Nairnshire"], [3, 2, 11050]], "sel": 2}`
- Error: logical-form mismatch

## test:6312:2-14655713-7

- Question: What is the highest yards when there are 0 INTs?
- Gold: `{"sel": 3, "conds": [[2, 2, 0]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[2, 0, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:6315:2-14655713-7

- Question: How many INTs are there with an average of 0 and more than 7 Sacks?
- Gold: `{"sel": 2, "conds": [[4, 0, 0], [1, 1, 7]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[4, 0, 0], [1, 1, 7]], "sel": 2}`
- Error: logical-form mismatch

## test:6319:2-14050649-3

- Question: How many Attendance has a Opponent of west bromwich albion, and a Result of 3 – 3, and a Match larger than 20?
- Gold: `{"sel": 5, "conds": [[2, 0, "west bromwich albion"], [4, 0, "3 – 3"], [0, 1, 20]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "west bromwich albion"], [4, 0, "3 – 3"], [0, 1, 20]], "sel": 5}`
- Error: logical-form mismatch

## test:6320:2-14050649-3

- Question: WHich Match has a Venue of h on 22 september 1888 with Attendances smaller than 4,000?
- Gold: `{"sel": 0, "conds": [[3, 0, "h"], [1, 0, "22 september 1888"], [5, 2, "4,000"]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "22 September 1888"], [3, 0, "H"], [5, 2, 4000]], "sel": 0}`
- Error: logical-form mismatch

## test:6324:2-14546530-7

- Question: what team scored 65-87
- Gold: `{"sel": 0, "conds": [[5, 0, "65-87"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "65-87"]], "sel": 1}`
- Error: logical-form mismatch

## test:6335:2-14445957-1

- Question: How much Preston North End has a Blackpool smaller than 0?
- Gold: `{"sel": 4, "conds": [[2, 2, 0]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[2, 2, 0]], "sel": 4}`
- Error: logical-form mismatch

## test:6336:2-14445957-1

- Question: Which Blackpool has a Preston North End smaller than 46, and a Competition of other, and a Draw larger than 1?
- Gold: `{"sel": 2, "conds": [[4, 2, 46], [0, 0, "other"], [3, 1, 1]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[4, 2, 46], [0, 0, "other"], [3, 1, 1]], "sel": 2}`
- Error: logical-form mismatch

## test:6347:2-14070062-2

- Question: Name the points with tries for of 40
- Gold: `{"sel": 4, "conds": [[6, 0, "40"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "40"]], "sel": 10}`
- Error: logical-form mismatch

## test:6363:2-14920900-1

- Question: What is the total silver when bronze is smaller than 0?
- Gold: `{"sel": 2, "conds": [[3, 2, 0]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[3, 2, 0]], "sel": 2}`
- Error: logical-form mismatch

## test:6365:2-14920900-1

- Question: What is the total when bronze has a silver larger than 2?
- Gold: `{"sel": 3, "conds": [[2, 1, 2]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[2, 1, 2]], "sel": 3}`
- Error: logical-form mismatch

## test:6373:2-14077277-3

- Question: Hoe many of lost have points greater than 14?
- Gold: `{"sel": 2, "conds": [[4, 1, 14]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 1, 14]], "sel": 2}`
- Error: logical-form mismatch

## test:6377:2-1453730-1

- Question: Which Bronze has a Total smaller than 2, and a Silver larger than 0, and a Gold smaller than 0?
- Gold: `{"sel": 4, "conds": [[5, 2, 2], [3, 1, 0], [2, 2, 0]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[5, 2, 2], [3, 1, 0], [2, 2, 0]], "sel": 4}`
- Error: logical-form mismatch

## test:6398:2-14271063-3

- Question: How many total drawn has less than 4 lost and 8 points?
- Gold: `{"sel": 1, "conds": [[2, 2, 4], [4, 0, 8]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 2, 4], [4, 0, 8]], "sel": 1}`
- Error: logical-form mismatch

## test:6399:2-14271063-3

- Question: How many lost are there before game 7?
- Gold: `{"sel": 2, "conds": [[0, 2, 7]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 2, 7]], "sel": 2}`
- Error: logical-form mismatch

## test:6400:2-14013061-1

- Question: How many touchdowns did the player with less than 4495 yards, long of less than 80, and yds/att less than 5.5 have?
- Gold: `{"sel": 5, "conds": [[3, 2, 4495], [6, 2, 80], [4, 2, 5.5]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 2, 4495], [6, 2, 80], [4, 2, 5.5]], "sel": 5}`
- Error: logical-form mismatch

## test:6401:2-14013061-1

- Question: How many attempts did the player ranking with a number higher than 1, who started after 1997 and had yds/att of 5 have?
- Gold: `{"sel": 2, "conds": [[7, 1, 1997], [4, 0, 5], [0, 1, 1]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 1, 1], [7, 1, 1997], [4, 0, 5]], "sel": 2}`
- Error: logical-form mismatch

## test:6417:2-1360997-4

- Question: What was the combined weight in kilograms of the horses in the race at Chelmsford stakes?
- Gold: `{"sel": 6, "conds": [[2, 0, "chelmsford stakes"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[2, 0, "Chelmsford Stakes"]], "sel": 6}`
- Error: logical-form mismatch

## test:6429:2-15117450-2

- Question: How many people went to the game that had 17-13?
- Gold: `{"sel": 5, "conds": [[2, 0, "17-13"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "17-13"]], "sel": 5}`
- Error: logical-form mismatch

## test:6438:2-14984039-1

- Question: What was the Attendance after Week 7 at Tiger Stadium?
- Gold: `{"sel": 6, "conds": [[5, 0, "tiger stadium"], [0, 1, 7]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 7], [5, 0, "Tiger Stadium"]], "sel": 6}`
- Error: logical-form mismatch

## test:6439:2-14984039-1

- Question: What was the Attendance at the Game with a Result of w 21–7?
- Gold: `{"sel": 6, "conds": [[3, 0, "w 21–7"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "w 21–7"]], "sel": 6}`
- Error: logical-form mismatch

## test:6472:2-136960-5

- Question: Who holds the time of 17:11.572?
- Gold: `{"sel": 0, "conds": [[6, 0, "17:11.572"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "17:11.572"]], "sel": 2}`
- Error: logical-form mismatch

## test:6473:2-136960-5

- Question: Who holds the time of 17:11.572?
- Gold: `{"sel": 0, "conds": [[6, 0, "17:11.572"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "17:11.572"]], "sel": 2}`
- Error: logical-form mismatch

## test:6477:2-13618358-1

- Question: Manufac turing b of 16.8, and a 2008 GDP per capita (USD) a smaller than 4,162, so what is the total number of mining b?
- Gold: `{"sel": 5, "conds": [[6, 0, 16.8], [3, 2, "4,162"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[6, 0, 16.8], [3, 2, 4162]], "sel": 5}`
- Error: logical-form mismatch

## test:6479:2-13618358-1

- Question: Income poverty f smaller than 13.6, and a Mining b of 1, and a Structural poverty g smaller than 7.8, so what is the total number of agriculture?
- Gold: `{"sel": 4, "conds": [[11, 2, 13.6], [5, 0, 1], [12, 2, 7.8]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[11, 2, 13.6], [5, 0, 1], [12, 2, 7.8]], "sel": 4}`
- Error: logical-form mismatch

## test:6482:2-15275060-1

- Question: What's the old Bulgarian word for avgust?
- Gold: `{"sel": 5, "conds": [[2, 0, "avgust"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Avgust"]], "sel": 3}`
- Error: logical-form mismatch

## test:6483:2-15275060-1

- Question: What's the old bulgarian word for октомври?
- Gold: `{"sel": 5, "conds": [[1, 0, "октомври"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Октомври"]], "sel": 3}`
- Error: logical-form mismatch

## test:6485:2-15275060-1

- Question: What's the old Bulgarian word for may?
- Gold: `{"sel": 5, "conds": [[0, 0, "may"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "May"]], "sel": 3}`
- Error: logical-form mismatch

## test:6493:2-14076814-5

- Question: How many Games has Points larger than 0 and a Lost smaller than 4?
- Gold: `{"sel": 0, "conds": [[4, 1, 0], [2, 2, 4], [1, 2, 0]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[4, 1, 0], [2, 2, 4]], "sel": 0}`
- Error: logical-form mismatch

## test:6500:2-13858035-1

- Question: How many specialists are at the college with more than 4 bachelor's degrees and more than 26 master's degrees?
- Gold: `{"sel": 4, "conds": [[1, 1, 4], [2, 1, 26]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[1, 1, 4], [2, 1, 26]], "sel": 4}`
- Error: logical-form mismatch

## test:6518:2-13844329-2

- Question: How many wins had Matches greater than 5?
- Gold: `{"sel": 2, "conds": [[1, 1, 5]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 1, 5]], "sel": 2}`
- Error: logical-form mismatch

## test:6529:2-15098383-3

- Question: What is the year that has points larger than 20?
- Gold: `{"sel": 0, "conds": [[3, 1, 20]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 1, 20]], "sel": 0}`
- Error: logical-form mismatch

## test:6533:2-14076980-2

- Question: How many drawn having more than 9 points?
- Gold: `{"sel": 1, "conds": [[4, 1, 9]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[4, 1, 9]], "sel": 1}`
- Error: logical-form mismatch

## test:6554:2-14781412-2

- Question: What year did the event in Hiroshima take place?
- Gold: `{"sel": 0, "conds": [[1, 0, "hiroshima"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Hiroshima"]], "sel": 0}`
- Error: logical-form mismatch

## test:6556:2-13912739-6

- Question: What is the game number of the game with the Edmonton Oilers as the opponent after February 12?
- Gold: `{"sel": 0, "conds": [[2, 0, "edmonton oilers"], [1, 1, 12]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Edmonton Oilers"], [1, 1, 12]], "sel": 0}`
- Error: logical-form mismatch

## test:6576:2-1434986-9

- Question: How much First elected has a Result of re-elected, and a Party of republican, and a District of illinois 4?
- Gold: `{"sel": 3, "conds": [[4, 0, "re-elected"], [2, 0, "republican"], [0, 0, "illinois 4"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "re-elected"], [2, 0, "republican"], [0, 0, "illinois 4"]], "sel": 3}`
- Error: logical-form mismatch

## test:6584:2-14369064-2

- Question: What is the number of silver medals of the team with 0 gold, ranked 5, and more than 0 bronze medals?
- Gold: `{"sel": 2, "conds": [[1, 0, 0], [0, 0, "5"], [3, 1, 0]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, 0], [0, 0, 5], [3, 1, 0]], "sel": 2}`
- Error: logical-form mismatch

## test:6587:2-1524433-1

- Question: What is the total number of top-25 that has a top-10 smaller than 4 with 0 cuts?
- Gold: `{"sel": 4, "conds": [[3, 2, 4], [6, 1, 0]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[3, 2, 4], [6, 0, 0]], "sel": 4}`
- Error: logical-form mismatch

## test:6589:2-1524433-1

- Question: What is the total for a top-10 in a masters tournament in an event smaller than 4?
- Gold: `{"sel": 3, "conds": [[0, 0, "masters tournament"], [5, 2, 4]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "Masters Tournament"], [5, 2, 4]], "sel": 3}`
- Error: logical-form mismatch

## test:6598:2-14345690-7

- Question: Which celebrity was famous for finishing 9th?
- Gold: `{"sel": 1, "conds": [[4, 0, "9th"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "9th"]], "sel": 0}`
- Error: logical-form mismatch

## test:6620:2-15073119-18

- Question: Which Cmp % has an Int smaller than 2 and a Cmpnsmaller than 1?
- Gold: `{"sel": 4, "conds": [[6, 2, 2], [2, 2, 1]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[6, 2, 2], [2, 2, 1]], "sel": 4}`
- Error: logical-form mismatch

## test:6621:2-15073119-18

- Question: How many Atts that have Yards of 43 and a Long larger than 43?
- Gold: `{"sel": 3, "conds": [[5, 0, 43], [7, 1, 43]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[5, 0, 43], [7, 1, 43]], "sel": 3}`
- Error: logical-form mismatch

## test:6622:2-15073119-18

- Question: How many Ints have a Rating smaller than 87, and Yards larger than 4?
- Gold: `{"sel": 6, "conds": [[1, 2, 87], [5, 1, 4]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[1, 2, 87], [5, 1, 4]], "sel": 6}`
- Error: logical-form mismatch

## test:6642:2-15198842-39

- Question: What was the Pick Number when the position was wide receiver, the college was Southern Miss with an overall less than 186?
- Gold: `{"sel": 1, "conds": [[4, 0, "wide receiver"], [5, 0, "southern miss"], [2, 2, 186]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "wide receiver"], [5, 0, "Southern Miss"], [2, 2, 186]], "sel": 1}`
- Error: logical-form mismatch

## test:6658:2-13564702-1

- Question: What is the Losing bonus with an extra try bonus?
- Gold: `{"sel": 9, "conds": [[8, 0, "try bonus"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[8, 0, "extra"]], "sel": 9}`
- Error: logical-form mismatch

## test:6703:2-15198842-22

- Question: What is the overall of the player with a pick # higher than 13?
- Gold: `{"sel": 2, "conds": [[1, 2, 13]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 1, 13]], "sel": 2}`
- Error: logical-form mismatch

## test:6734:2-13648477-1

- Question: What is the total number for grid with a Suzuki GSX-R1000 K7 for +13.283?
- Gold: `{"sel": 4, "conds": [[1, 0, "suzuki gsx-r1000 k7"], [3, 0, "+13.283"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "Suzuki GSX-R1000 K7"], [3, 0, "+13.283"]], "sel": 4}`
- Error: logical-form mismatch

## test:6738:2-14407512-23

- Question: How many points have less than 126 2nd and nationality of aut?
- Gold: `{"sel": 5, "conds": [[4, 2, 126], [2, 0, "aut"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[4, 2, 126], [2, 0, "AUT"]], "sel": 5}`
- Error: logical-form mismatch

## test:6740:2-1460129-1

- Question: Which act's album has a name of All That You Can't Leave Behind?
- Gold: `{"sel": 5, "conds": [[4, 0, "all that you can't leave behind"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "All That You Can't Leave Behind"]], "sel": 3}`
- Error: logical-form mismatch

## test:6749:2-13638416-3

- Question: what week had a player named zach
- Gold: `{"sel": 3, "conds": [[0, 0, "zach"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "zach"]], "sel": 1}`
- Error: logical-form mismatch

## test:6763:2-14344407-3

- Question: Which November has a Game smaller than 16, and Points larger than 22?
- Gold: `{"sel": 1, "conds": [[0, 2, 16], [5, 1, 22]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 2, 16], [5, 1, 22]], "sel": 1}`
- Error: logical-form mismatch

## test:6802:2-16168849-1

- Question: What is the total number of teams founded that were left in 1976?
- Gold: `{"sel": 2, "conds": [[7, 0, "1976"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[7, 0, "1976"]], "sel": 2}`
- Error: logical-form mismatch

## test:6816:2-15315989-2

- Question: Which Lost has Points of 28 and a Drawn smaller than 8?
- Gold: `{"sel": 5, "conds": [[2, 0, 28], [4, 2, 8]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 0, 28], [4, 2, 8]], "sel": 5}`
- Error: logical-form mismatch

## test:6822:2-15640438-3

- Question: What was the Attendance on 31 January 1987?
- Gold: `{"sel": 4, "conds": [[0, 0, "31 january 1987"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "31 January 1987"]], "sel": 4}`
- Error: logical-form mismatch

## test:6827:2-15463188-16

- Question: Who is the position for the 2009-2010 season, number 1?
- Gold: `{"sel": 1, "conds": [[4, 0, "2009-2010"], [2, 0, "1"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "2009-2010"], [2, 0, "1"]], "sel": 1}`
- Error: logical-form mismatch

## test:6854:2-1577834-1

- Question: Which Draw has a Season of 2001–02, and Points larger than 47?
- Gold: `{"sel": 2, "conds": [[0, 0, "2001–02"], [4, 1, 47]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "2001–02"], [4, 1, 47]], "sel": 2}`
- Error: logical-form mismatch

## test:6870:2-15679259-3

- Question: What conference is the 1973-74 team in the Atlantic Division (Div.)?
- Gold: `{"sel": 2, "conds": [[3, 0, "atlantic"], [1, 0, "1973-74"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "1973-74"], [3, 0, "Atlantic"]], "sel": 2}`
- Error: logical-form mismatch

## test:6889:2-15859432-2

- Question: What is the total number of Block for the Player with less than 85 Weight and more than 187 Height?
- Gold: `{"sel": 5, "conds": [[3, 2, 85], [2, 1, 187]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[3, 2, 85], [2, 1, 187]], "sel": 5}`
- Error: logical-form mismatch

## test:6891:2-15859432-2

- Question: What is the Weight of the player with a Block larger than 328, Spike greater than 375 and Height larger than 207?
- Gold: `{"sel": 3, "conds": [[5, 1, 328], [2, 1, 207], [4, 1, 375]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 1, 328], [4, 1, 375], [2, 1, 207]], "sel": 3}`
- Error: logical-form mismatch

## test:6914:2-15514527-7

- Question: Which Against has a Peel of waroona, and a Byes larger than 0?
- Gold: `{"sel": 5, "conds": [[0, 0, "waroona"], [2, 1, 0]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "waroona"], [2, 1, 0]], "sel": 5}`
- Error: logical-form mismatch

## test:6915:2-15514527-7

- Question: Which Draws has a Wins smaller than 17, and an Against smaller than 1158?
- Gold: `{"sel": 4, "conds": [[1, 2, 17], [5, 2, 1158]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 2, 17], [5, 2, 1158]], "sel": 4}`
- Error: logical-form mismatch

## test:6916:2-15514527-7

- Question: Which Draws has an Against larger than 1158, and a Wins of 9, and a Losses smaller than 9?
- Gold: `{"sel": 4, "conds": [[5, 1, 1158], [1, 0, 9], [3, 2, 9]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[5, 1, 1158], [1, 0, 9], [3, 2, 9]], "sel": 4}`
- Error: logical-form mismatch

## test:6917:2-15514527-7

- Question: Which Losses has a Wins of 6, and an Against smaller than 1741?
- Gold: `{"sel": 3, "conds": [[1, 0, 6], [5, 2, 1741]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[1, 0, 6], [5, 2, 1741]], "sel": 3}`
- Error: logical-form mismatch

## test:6950:2-15700367-6

- Question: What is the total number of Maidens when E.R. is less than 9.5, and a Overs Bowled larger than 57, and a Wickets of 9?
- Gold: `{"sel": 2, "conds": [[6, 2, 9.5], [1, 1, 57], [4, 0, 9]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[6, 2, 9.5], [1, 1, 57], [4, 0, 9]], "sel": 2}`
- Error: logical-form mismatch

## test:6952:2-15566586-4

- Question: How many FA Trophies had a total of 27, 2 FA cups, and a league larger than 24?
- Gold: `{"sel": 4, "conds": [[6, 0, 27], [3, 0, 2], [2, 1, 24]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[6, 0, 27], [3, 0, 2], [2, 1, 24]], "sel": 4}`
- Error: logical-form mismatch

## test:6965:2-160728-7

- Question: What is the Tamil Name of சந்திர புத்தாண்டு (தினம் 2)?
- Gold: `{"sel": 4, "conds": [[3, 0, "சந்திர புத்தாண்டு (தினம் 2)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "சந்திர புத்தாண்டு (தினம் 2)"]], "sel": 3}`
- Error: logical-form mismatch

## test:6998:2-15988037-17

- Question: What is the total rank of the celebrity with a 34.66 average and a season greater than 1?
- Gold: `{"sel": 0, "conds": [[4, 0, 34.66], [3, 1, 1]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[4, 0, 34.66], [3, 1, 1]], "sel": 0}`
- Error: logical-form mismatch

## test:7009:2-15547723-1

- Question: What is the total University of Dublin value with a labour panel greater than 11?
- Gold: `{"sel": 6, "conds": [[4, 1, 11]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[4, 1, 11]], "sel": 6}`
- Error: logical-form mismatch

## test:7058:2-15618241-1

- Question: How many winner's shares have ai miyazato as the champion?
- Gold: `{"sel": 8, "conds": [[2, 0, "ai miyazato"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "Ai Miyazato"]], "sel": 8}`
- Error: logical-form mismatch

## test:7081:2-16078390-2

- Question: What is the Enrollment for the Coyotes Founded in 1891?
- Gold: `{"sel": 4, "conds": [[2, 0, 1891], [5, 0, "coyotes"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "Coyotes"], [2, 0, 1891]], "sel": 4}`
- Error: logical-form mismatch

## test:7084:2-16078390-2

- Question: What is the Enrollment at Whitman College Founded after 1859?
- Gold: `{"sel": 4, "conds": [[0, 0, "whitman college"], [2, 1, 1859]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Whitman College"], [2, 1, 1859]], "sel": 4}`
- Error: logical-form mismatch

## test:7085:2-15524351-17

- Question: What was the attendance when the opponent was virginia?
- Gold: `{"sel": 4, "conds": [[1, 0, "virginia"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Virginia"]], "sel": 4}`
- Error: logical-form mismatch

## test:7092:2-15611271-20

- Question: What is the total number of avg/g with a long of 50, a gp-gs of 3-0, and 926 yards?
- Gold: `{"sel": 4, "conds": [[3, 0, 50], [1, 0, "3-0"], [2, 1, 926]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[3, 0, 50], [1, 0, "3-0"], [2, 0, 926]], "sel": 4}`
- Error: logical-form mismatch

## test:7099:2-15430129-2

- Question: How many match values have points under 14 and 0 draws?
- Gold: `{"sel": 1, "conds": [[2, 2, 14], [3, 2, 0]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[2, 2, 14], [3, 0, 0]], "sel": 1}`
- Error: logical-form mismatch

## test:7109:2-15739098-1

- Question: What is the Director for the episode titled “some lapse of time”?
- Gold: `{"sel": 4, "conds": [[1, 0, "“some lapse of time”"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "some lapse of time"]], "sel": 4}`
- Error: logical-form mismatch

## test:7110:2-15739098-1

- Question: What is the Airdate for the episode titled “thirteen to centaurus” Adapted by stanley miller?
- Gold: `{"sel": 5, "conds": [[3, 0, "stanley miller"], [1, 0, "“thirteen to centaurus”"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Thirteen to Centaurus"], [3, 0, "Stanley Miller"]], "sel": 5}`
- Error: logical-form mismatch

## test:7113:2-1597347-1

- Question: What 2007 number when the million CZK shows operating revenues?
- Gold: `{"sel": 3, "conds": [[0, 0, "operating revenues"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Operating revenues"]], "sel": 3}`
- Error: logical-form mismatch

## test:7125:2-15777504-1

- Question: What is the total bronze medals won, with 0 gold medals and in 5th place?
- Gold: `{"sel": 2, "conds": [[0, 0, 0], [4, 2, 0]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 0, 0], [4, 0, 5]], "sel": 2}`
- Error: logical-form mismatch

## test:7130:2-15343730-1

- Question: How many years have a conventional plan of 7%?
- Gold: `{"sel": 0, "conds": [[1, 0, "7%"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "7%"]], "sel": 0}`
- Error: logical-form mismatch

## test:7133:2-15547329-1

- Question: How many are on the administrative panel with an agricultural panel of fewer than 11 and an industrial and commercial panel of 3, with fewer than 4 on the labor panel?
- Gold: `{"sel": 0, "conds": [[1, 2, 11], [3, 0, 3], [4, 2, 4]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[1, 2, 11], [3, 0, 3], [4, 2, 4]], "sel": 0}`
- Error: logical-form mismatch

## test:7174:2-15753220-15

- Question: What is the total weight of players who play the G position for the Los Angeles D-Fenders?
- Gold: `{"sel": 4, "conds": [[0, 0, "g"], [2, 0, "los angeles d-fenders"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "G"], [2, 0, "Los Angeles D-Fenders"]], "sel": 4}`
- Error: logical-form mismatch

## test:7177:2-15567091-4

- Question: What is the total of the FA CUP that has 1 FA trophy, and player Chris Cook, and a League cup less than 1?
- Gold: `{"sel": 3, "conds": [[4, 0, 1], [0, 0, "chris cook"], [5, 2, 1]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[4, 0, 1], [0, 0, "Chris Cook"], [5, 2, 1]], "sel": 3}`
- Error: logical-form mismatch

## test:7188:2-1588821-4

- Question: How many floors have 207 w. hastings st. as the address?
- Gold: `{"sel": 4, "conds": [[1, 0, "207 w. hastings st."]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "207 W. Hastings St."]], "sel": 4}`
- Error: logical-form mismatch

## test:7221:2-1588821-1

- Question: What is the number of floors that have years under 2008 and were named Guinness Tower?
- Gold: `{"sel": 3, "conds": [[4, 2, 2008], [1, 0, "guinness tower"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 2, 2008], [1, 0, "Guinness Tower"]], "sel": 3}`
- Error: logical-form mismatch

## test:7234:2-15354254-1

- Question: What is the total number of points where there were 3 losses and a played number bigger than 12?
- Gold: `{"sel": 2, "conds": [[5, 0, 3], [3, 1, 12]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[5, 0, 3], [3, 1, 12]], "sel": 2}`
- Error: logical-form mismatch

## test:7241:2-15405394-1

- Question: How many Drawns have a Team of aa são bento and Points larger than 1?
- Gold: `{"sel": 4, "conds": [[1, 0, "aa são bento"], [2, 1, 1]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "aa são bento"], [2, 1, 1]], "sel": 4}`
- Error: logical-form mismatch

## test:7243:2-15405394-1

- Question: How many Against has a Drawn smaller than 1, and a Lost smaller than 5?
- Gold: `{"sel": 6, "conds": [[4, 2, 1], [5, 2, 5]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[4, 2, 1], [5, 2, 5]], "sel": 6}`
- Error: logical-form mismatch

## test:7245:2-1590321-51

- Question: How many goals were there for Johan Cruyff when the rank's less than 3?
- Gold: `{"sel": 4, "conds": [[1, 0, "johan cruyff"], [0, 2, 3]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Johan Cruyff"], [0, 2, 3]], "sel": 4}`
- Error: logical-form mismatch

## test:7252:2-16050349-3

- Question: With more than 69 Assists, what is Dejuan Collins' Rank?
- Gold: `{"sel": 0, "conds": [[1, 0, "dejuan collins"], [4, 1, 69]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 1, 69], [1, 0, "Dejuan Collins"]], "sel": 0}`
- Error: logical-form mismatch

## test:7267:2-15416653-1

- Question: What is the total number of ranks when the Peak Name is Red Shirt Table?
- Gold: `{"sel": 0, "conds": [[3, 0, "red shirt table"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "Red Shirt Table"]], "sel": 0}`
- Error: logical-form mismatch

## test:7298:2-16147528-6

- Question: How many holes does Player Vijay Singh have?
- Gold: `{"sel": 4, "conds": [[1, 0, "vijay singh"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Vijay Singh"]], "sel": 4}`
- Error: logical-form mismatch

## test:7299:2-16147528-6

- Question: How many holes does Player Vijay Singh have?
- Gold: `{"sel": 4, "conds": [[1, 0, "vijay singh"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Vijay Singh"]], "sel": 4}`
- Error: logical-form mismatch

## test:7300:2-15701357-4

- Question: On what frequency does W233AG broadcast?
- Gold: `{"sel": 1, "conds": [[0, 0, "w233ag"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "W233AG"]], "sel": 1}`
- Error: logical-form mismatch

## test:7311:2-16023812-2

- Question: How many people attended the game played with the New England Patriots as opponents?
- Gold: `{"sel": 4, "conds": [[2, 0, "new england patriots"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "new england patriots"]], "sel": 4}`
- Error: logical-form mismatch

## test:7346:2-15653040-1

- Question: How many people live where there are 118% of people have phones?
- Gold: `{"sel": 2, "conds": [[3, 0, 118]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, 118]], "sel": 2}`
- Error: logical-form mismatch

## test:7350:2-15409776-3

- Question: How many silver medals were awarded to the Nation with less than 2 gold, more than 6 bronze and a rank higher than 5?
- Gold: `{"sel": 3, "conds": [[0, 1, 5], [4, 1, 6], [2, 2, 2]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 2, 2], [4, 1, 6], [0, 1, 5]], "sel": 3}`
- Error: logical-form mismatch

## test:7353:2-1532779-1

- Question: What is the number of registered mosques with a population of England and Wales greater than 46,196 in a year before 1971?
- Gold: `{"sel": 4, "conds": [[2, 1, "46,196"], [0, 2, 1971]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 1, "46,196"], [0, 2, 1971]], "sel": 4}`
- Error: logical-form mismatch

## test:7374:2-15914761-1

- Question: On what date did the audience of 60,092 people watched a game end with a W 21-9?
- Gold: `{"sel": 1, "conds": [[4, 1, "60,092"], [3, 0, "w 21-9"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "60,092"], [3, 0, "W 21-9"]], "sel": 1}`
- Error: logical-form mismatch

## test:7375:2-15914761-1

- Question: What week did the Atlanta Falcons play in front of less than 59,743 people?
- Gold: `{"sel": 0, "conds": [[4, 2, "59,743"], [2, 0, "atlanta falcons"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Atlanta Falcons"], [4, 2, 59743]], "sel": 0}`
- Error: logical-form mismatch

## test:7387:2-15715109-40

- Question: What is the total weight (km) that has a 1983-1984 team of washington capitals, Bryan Erickson as the name, with a jersey # greater than 24?
- Gold: `{"sel": 4, "conds": [[7, 0, "washington capitals"], [2, 0, "bryan erickson"], [1, 1, 24]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[7, 0, "washington capitals"], [2, 0, "bryan erickson"], [1, 1, 24]], "sel": 4}`
- Error: logical-form mismatch

## test:7405:2-1618358-1

- Question: What is the Total Tax Revenue that has an n.a. Stamp Duty Reserve Tax in the years 1995-96?
- Gold: `{"sel": 4, "conds": [[1, 0, "n.a."], [0, 0, "1995-96"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "n.a."], [0, 0, "1995-96"]], "sel": 3}`
- Error: logical-form mismatch

## test:7418:2-15765416-1

- Question: How many weeks have l 3-17 as the result?
- Gold: `{"sel": 0, "conds": [[3, 0, "l 3-17"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "l 3-17"]], "sel": 0}`
- Error: logical-form mismatch

## test:7446:2-16082306-6

- Question: What is the total 3FG Pct of the player with a FG Pct greater than 43.2, a FT Pct less than 100, a total reb less than 102, and a 3FGM of 1?
- Gold: `{"sel": 4, "conds": [[1, 1, 43.2], [5, 2, 100], [8, 2, 102], [2, 0, 1]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 1, 43.2], [5, 2, 100], [8, 2, 102], [2, 0, 1]], "sel": 4}`
- Error: logical-form mismatch

## test:7451:2-16176685-5

- Question: How many Games has a Name of stéphane dumas and a Rank larger than 5?
- Gold: `{"sel": 3, "conds": [[1, 0, "stéphane dumas"], [0, 1, 5]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "stéphane dumas"], [0, 1, 5]], "sel": 3}`
- Error: logical-form mismatch

## test:7452:2-16176685-5

- Question: How many Games has a Team of cai zaragoza and a Rank smaller than 1?
- Gold: `{"sel": 3, "conds": [[2, 0, "cai zaragoza"], [0, 2, 1]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "cai zaragoza"], [0, 2, 1]], "sel": 3}`
- Error: logical-form mismatch

## test:7466:2-15331868-1

- Question: Which Lost has Points smaller than 12, and a Drawn larger than 1?
- Gold: `{"sel": 5, "conds": [[2, 2, 12], [4, 1, 1]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 2, 12], [4, 1, 1]], "sel": 5}`
- Error: logical-form mismatch

## test:7467:2-15331868-1

- Question: Which Position has a Difference of 5, and a Drawn smaller than 3?
- Gold: `{"sel": 0, "conds": [[7, 0, "5"], [4, 2, 3]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[7, 0, "5"], [4, 2, 3]], "sel": 0}`
- Error: logical-form mismatch

## test:7468:2-15331868-1

- Question: Which Against has a Position larger than 11?
- Gold: `{"sel": 6, "conds": [[0, 1, 11]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 1, 11]], "sel": 6}`
- Error: logical-form mismatch

## test:7480:2-16181798-1

- Question: How many numbers of languages were there for issues with circulation of 44,748,000?
- Gold: `{"sel": 3, "conds": [[2, 0, "44,748,000"]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "44,748,000"]], "sel": 3}`
- Error: logical-form mismatch

## test:7490:2-1618788-2

- Question: How many points total are there later than 2003?
- Gold: `{"sel": 4, "conds": [[0, 1, 2003]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 1, 2003]], "sel": 4}`
- Error: logical-form mismatch

## test:7509:2-16065919-4

- Question: What is Metodija Gogov's Start of Reign?
- Gold: `{"sel": 1, "conds": [[3, 0, "metodija gogov"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Metodija Gogov"]], "sel": 1}`
- Error: logical-form mismatch

## test:7537:2-15386342-2

- Question: What is the highest week for Cleveland Browns with 54,205 in attendance?
- Gold: `{"sel": 0, "conds": [[2, 0, "cleveland browns"], [4, 1, "54,205"]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[2, 0, "Cleveland Browns"], [4, 0, 54205]], "sel": 0}`
- Error: logical-form mismatch

## test:7543:2-16181680-2

- Question: What is the total lane number for the United States when the mark is 6.62 and the heat is greater than 8?
- Gold: `{"sel": 1, "conds": [[3, 0, "united states"], [4, 0, "6.62"], [0, 1, 8]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[3, 0, "United States"], [4, 0, "6.62"], [0, 1, 8]], "sel": 1}`
- Error: logical-form mismatch

## test:7564:2-15524351-9

- Question: What was the total attendance on 10/05/1974?
- Gold: `{"sel": 4, "conds": [[0, 0, "10/05/1974"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "10/05/1974"]], "sel": 4}`
- Error: logical-form mismatch

## test:7572:2-15331084-1

- Question: What is the position number when there were 29 points, and less than 2 is lost?
- Gold: `{"sel": 0, "conds": [[2, 0, 29], [5, 2, 2]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, 29], [5, 2, 2]], "sel": 0}`
- Error: logical-form mismatch

## test:7579:2-15780049-5

- Question: What is the game number when the score was l 90–104 (ot)?
- Gold: `{"sel": 0, "conds": [[3, 0, "l 90–104 (ot)"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "L 90–104 (OT)"]], "sel": 0}`
- Error: logical-form mismatch

## test:7585:2-15379441-1

- Question: What is the number for gold where there were total 1, and bronze 1?
- Gold: `{"sel": 2, "conds": [[5, 0, 1], [4, 0, 1]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[5, 0, 1], [4, 0, 1]], "sel": 2}`
- Error: logical-form mismatch

## test:7589:2-16147528-3

- Question: Which player won in 1987 and ended with a score of +9?
- Gold: `{"sel": 3, "conds": [[4, 0, "+9"], [2, 0, "1987"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "1987"], [4, 0, "+9"]], "sel": 0}`
- Error: logical-form mismatch

## test:7600:2-16002877-1

- Question: What is the fewest number of silvers have 0 golds?
- Gold: `{"sel": 3, "conds": [[2, 2, 0]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[2, 0, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:7604:2-1560445-2

- Question: What is the average for the 1990s with a total of 1, and 0 in the 1980s?
- Gold: `{"sel": 8, "conds": [[10, 0, 1], [7, 2, 0]], "agg": 5}`
- Prediction: `{"agg": 5, "conds": [[10, 0, 1], [7, 0, 0]], "sel": 8}`
- Error: logical-form mismatch

## test:7605:2-1560445-2

- Question: What is the sum for the 2000s to date that has 0 in the 1920s?
- Gold: `{"sel": 9, "conds": [[1, 2, 0]], "agg": 4}`
- Prediction: `{"agg": 4, "conds": [[1, 0, 0]], "sel": 9}`
- Error: logical-form mismatch

## test:7606:2-1560445-2

- Question: What is the total number in the 1920s that has 0 in the 1960s, and less than 4 in the 2000s, and more than 3 in the 1930s?
- Gold: `{"sel": 1, "conds": [[5, 0, 0], [9, 2, 4], [2, 1, 3]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[5, 0, 0], [9, 2, 4], [2, 1, 3]], "sel": 1}`
- Error: logical-form mismatch

## test:7607:2-1560445-2

- Question: What was the sum for the 1990s, that has 0 in the 1900s?
- Gold: `{"sel": 8, "conds": [[0, 2, 0]], "agg": 4}`
- Prediction: `{"agg": 4, "conds": [[0, 0, 0]], "sel": 8}`
- Error: logical-form mismatch

## test:7652:2-16050349-1

- Question: What is the total rank of team roanne, which has less than 14 games?
- Gold: `{"sel": 0, "conds": [[2, 0, "roanne"], [3, 2, 14]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[2, 0, "Roanne"], [3, 2, 14]], "sel": 0}`
- Error: logical-form mismatch

## test:7669:2-15696410-1

- Question: How many draws did gary o'shaughnessy have?
- Gold: `{"sel": 0, "conds": [[2, 0, "gary o'shaughnessy"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "gary o'shaughnessy"]], "sel": 0}`
- Error: logical-form mismatch

## test:7693:2-156359-1

- Question: What kind of Silver has a Nation of norway and a Gold smaller than 3?
- Gold: `{"sel": 3, "conds": [[1, 0, "norway"], [2, 2, 3]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Norway"], [2, 2, 3]], "sel": 3}`
- Error: logical-form mismatch

## test:7710:2-15598908-5

- Question: Which Yards has a Long smaller than 3?
- Gold: `{"sel": 2, "conds": [[4, 2, 3]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 2, 3]], "sel": 2}`
- Error: logical-form mismatch

## test:7746:2-15483861-1

- Question: With an in-state area of 053 1,654km 2 639mi 2, what is the total area?
- Gold: `{"sel": 2, "conds": [[3, 0, "053 1,654km 2 639mi 2"]], "agg": 0}`
- Prediction: `{"agg": 4, "conds": [[3, 0, "053 1,654km 2 639mi 2"]], "sel": 2}`
- Error: logical-form mismatch

## test:7765:2-15322952-2

- Question: What is the total number of Dates during which the Catalog nebbc003 was given?
- Gold: `{"sel": 1, "conds": [[4, 0, "nebbc003"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "nebbc003"]], "sel": 1}`
- Error: logical-form mismatch

## test:7851:2-16729457-1

- Question: What is the lowest number of participants in 2010 when there were 0 participants in 2012?
- Gold: `{"sel": 1, "conds": [[3, 2, 0]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[3, 0, 0]], "sel": 1}`
- Error: logical-form mismatch

## test:7856:2-17085981-1

- Question: What is the Capacity of the Rainer Kraft's Stadium?
- Gold: `{"sel": 4, "conds": [[1, 0, "rainer kraft"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Rainer Kraft"]], "sel": 4}`
- Error: logical-form mismatch

## test:7876:2-17128242-4

- Question: WHAT IS THE PLACE THAT HAS SCORE OF 65 OR BETTER, FOR ROCCO MEDIATE?
- Gold: `{"sel": 0, "conds": [[3, 1, 65], [1, 0, "rocco mediate"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 2, 65], [1, 0, "Rocco Mediate"]], "sel": 0}`
- Error: logical-form mismatch

## test:7879:2-17611995-35

- Question: What is the number of cups when the other was more than 3, the league more than 3, for Lauri Dalla Valle, and a Total more than 21?
- Gold: `{"sel": 2, "conds": [[3, 1, 3], [1, 1, 3], [0, 0, "lauri dalla valle"], [4, 1, 21]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[3, 1, 3], [1, 1, 3], [0, 0, "Lauri Dalla Valle"], [4, 1, 21]], "sel": 2}`
- Error: logical-form mismatch

## test:7880:2-17611995-35

- Question: What is the number for other when Adam Pepper is the player with a total more than 7?
- Gold: `{"sel": 3, "conds": [[0, 0, "adam pepper"], [4, 1, 7]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Adam Pepper"], [4, 1, 7]], "sel": 3}`
- Error: logical-form mismatch

## test:7884:2-17421790-2

- Question: What is the total amount of points for a position less than 7, 68 goals for, and less than 30 played?
- Gold: `{"sel": 3, "conds": [[0, 2, 7], [7, 0, 68], [2, 2, 30]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 2, 7], [7, 0, 68], [2, 2, 30]], "sel": 3}`
- Error: logical-form mismatch

## test:7885:2-17421790-2

- Question: What is teh average amount of goals for club real avilés cf, which has more than 59 goals against and a -10 goal difference?
- Gold: `{"sel": 7, "conds": [[8, 1, 59], [1, 0, "real avilés cf"], [9, 1, -10]], "agg": 5}`
- Prediction: `{"agg": 5, "conds": [[1, 0, "Real Avilés CF"], [8, 1, 59], [9, 0, -10]], "sel": 7}`
- Error: logical-form mismatch

## test:7899:2-17058178-1

- Question: WHAT WAS THE PICK NUMBER FOR BRANDON RUSH?
- Gold: `{"sel": 1, "conds": [[2, 0, "brandon rush"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Brandon Rush"]], "sel": 1}`
- Error: logical-form mismatch

## test:7907:2-1666310-6

- Question: How many floors did the building at the Jewellery quarter have?
- Gold: `{"sel": 4, "conds": [[1, 0, "jewellery quarter"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "Jewellery quarter"]], "sel": 4}`
- Error: logical-form mismatch

## test:7912:2-17529767-9

- Question: Can you tell me the total number of 100s that has the Balls larger than 325, and the Runs smaller than 572?
- Gold: `{"sel": 7, "conds": [[4, 1, 325], [3, 2, 572]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[4, 1, 325], [3, 2, 572]], "sel": 7}`
- Error: logical-form mismatch

## test:7924:2-17344644-1

- Question: What round was jerry corcoran drafted in as pick number 114?
- Gold: `{"sel": 0, "conds": [[1, 1, 114], [2, 0, "jerry corcoran"]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[1, 0, 114], [2, 0, "jerry corcoran"]], "sel": 0}`
- Error: logical-form mismatch

## test:7926:2-17344644-1

- Question: Who was the highest drafted player that attended college at Virginia?
- Gold: `{"sel": 1, "conds": [[4, 0, "virginia"]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "virginia"]], "sel": 2}`
- Error: logical-form mismatch

## test:8006:2-16410647-3

- Question: Which frequency belongs to the beat branding?
- Gold: `{"sel": 0, "conds": [[2, 0, "the beat"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "beat"]], "sel": 0}`
- Error: logical-form mismatch

## test:8013:2-16763649-1

- Question: WHAT YEAR WAS ROBERT COOMBES CHAMPION ON MAY 7?
- Gold: `{"sel": 0, "conds": [[2, 0, "robert coombes"], [1, 0, "may 7"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "May 7"], [2, 0, "Robert Coombes"]], "sel": 0}`
- Error: logical-form mismatch

## test:8049:2-16649508-1

- Question: Which 92.5 holds the world record?
- Gold: `{"sel": 0, "conds": [[1, 0, "92.5"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "92.5"]], "sel": 2}`
- Error: logical-form mismatch

## test:8063:2-1688640-20

- Question: WHAT WAS THE LOWEST CAR # WITH SON-E-WA, AND 2012 START YEAR?
- Gold: `{"sel": 3, "conds": [[2, 0, "son-e-wa"], [0, 2, 2012]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[2, 0, "son-e-wa"], [0, 0, 2012]], "sel": 3}`
- Error: logical-form mismatch

## test:8077:2-16710848-2

- Question: Who are the opponents with a record of 3-0?
- Gold: `{"sel": 5, "conds": [[6, 0, "3-0"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "3-0"]], "sel": 2}`
- Error: logical-form mismatch

## test:8131:2-174003-4

- Question: What is the weight when the race was the VRC Melbourne Cup?
- Gold: `{"sel": 3, "conds": [[1, 0, "vrc melbourne cup"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "VRC Melbourne Cup"]], "sel": 3}`
- Error: logical-form mismatch

## test:8135:2-17100961-84

- Question: what is the pick for alfred morris when the overall is less than 217, and the round is smaller than 6?
- Gold: `{"sel": 1, "conds": [[2, 2, 217], [3, 0, "alfred morris"], [0, 2, 6]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Alfred Morris"], [2, 2, 217], [0, 2, 6]], "sel": 1}`
- Error: logical-form mismatch

## test:8184:2-17305625-2

- Question: Which Inhabitants has a Party of south tyrolean people's party, a Municipality of bruneck, and an Election larger than 2010?
- Gold: `{"sel": 1, "conds": [[3, 0, "south tyrolean people's party"], [0, 0, "bruneck"], [4, 1, 2010]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "south tyrolean people's party"], [0, 0, "bruneck"], [4, 1, 2010]], "sel": 1}`
- Error: logical-form mismatch

## test:8185:2-17305625-2

- Question: Which Election has a Municipality of laives, and Inhabitants smaller than 17,197?
- Gold: `{"sel": 4, "conds": [[0, 0, "laives"], [1, 2, "17,197"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "laives"], [1, 2, "17,197"]], "sel": 4}`
- Error: logical-form mismatch

## test:8211:2-1640927-1

- Question: COunt the Founded which has a Venue of villa park?
- Gold: `{"sel": 2, "conds": [[4, 0, "villa park"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "villa park"]], "sel": 2}`
- Error: logical-form mismatch

## test:8221:2-16406300-1

- Question: What was the total Attendance in weeks previous of 5, playing the Seattle Seahawks?
- Gold: `{"sel": 4, "conds": [[0, 2, 5], [2, 0, "seattle seahawks"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 2, 5], [2, 0, "Seattle Seahawks"]], "sel": 4}`
- Error: logical-form mismatch

## test:8245:2-1730453-1

- Question: What type of office left office in 1810?
- Gold: `{"sel": 0, "conds": [[4, 0, "1810"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "1810"]], "sel": 1}`
- Error: logical-form mismatch

## test:8264:2-16360419-1

- Question: How many gold when silver is less than 32, bronze is 25, and overall is less than 67?
- Gold: `{"sel": 1, "conds": [[2, 2, 32], [3, 0, 25], [4, 2, 67]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 2, 32], [3, 0, 25], [4, 2, 67]], "sel": 1}`
- Error: logical-form mismatch

## test:8265:2-16360419-1

- Question: How many silver when bronze is 25 and overall is less than 67?
- Gold: `{"sel": 2, "conds": [[3, 0, 25], [4, 2, 67]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[3, 0, 25], [4, 2, 67]], "sel": 2}`
- Error: logical-form mismatch

## test:8312:2-17611995-20

- Question: What is the total PL G of player pennant, who has less than 7 CL G, less than 7 CL apps, and a FA YC of 0?
- Gold: `{"sel": 2, "conds": [[4, 2, 7], [3, 2, 7], [9, 0, 0], [0, 0, "pennant"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "Pennant"], [4, 2, 7], [3, 2, 7], [9, 0, 0]], "sel": 2}`
- Error: logical-form mismatch

## test:8353:2-17001488-3

- Question: What is Driver, when Race 2 is "10"?
- Gold: `{"sel": 0, "conds": [[4, 0, "10"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "10"]], "sel": 0}`
- Error: logical-form mismatch

## test:8358:2-16900662-8

- Question: WHAT YEAR WAS AT GIANTS STADIUM, WITH WINNER OF NEW YORK GIANTS?
- Gold: `{"sel": 0, "conds": [[5, 0, "giants stadium"], [2, 0, "new york giants"]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "Giants Stadium"], [2, 0, "New York Giants"]], "sel": 0}`
- Error: logical-form mismatch

## test:8373:2-1620220-3

- Question: What is the label for the CD format in North America?
- Gold: `{"sel": 2, "conds": [[4, 0, "cd"], [1, 0, "north america"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "CD"], [1, 0, "North America"]], "sel": 2}`
- Error: logical-form mismatch

## test:8411:2-17256960-6

- Question: Where did Day & Age rank in the Rolling Stone in 2008?
- Gold: `{"sel": 4, "conds": [[0, 0, "rolling stone"], [3, 0, 2008]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Rolling Stone"], [3, 0, 2008]], "sel": 4}`
- Error: logical-form mismatch

## test:8412:2-17256960-6

- Question: What country did Day & Age rank number 1 in Q prior to 2011?
- Gold: `{"sel": 1, "conds": [[3, 2, 2011], [4, 1, 1], [0, 0, "q"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Q"], [3, 2, 2011], [4, 0, 1]], "sel": 1}`
- Error: logical-form mismatch

## test:8437:2-16764781-2

- Question: How many people attended the game on week 3?
- Gold: `{"sel": 5, "conds": [[0, 0, 3]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 3]], "sel": 5}`
- Error: logical-form mismatch

## test:8509:2-16931017-3

- Question: Which Capacity has a School of windlehurst school, and an Ofsted smaller than 131889?
- Gold: `{"sel": 3, "conds": [[0, 0, "windlehurst school"], [4, 2, 131889]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "windlehurst school"], [4, 2, 131889]], "sel": 3}`
- Error: logical-form mismatch

## test:8533:2-17471011-1

- Question: What year had a black of Kramnik, opening of E05 Catalan Opening, moves greater than 38, and a result of ½–½?
- Gold: `{"sel": 2, "conds": [[3, 0, "½–½"], [1, 0, "kramnik"], [6, 0, "e05 catalan opening"], [4, 1, 38]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Kramnik"], [6, 0, "E05 Catalan Opening"], [4, 1, 38], [3, 0, "½–½"]], "sel": 2}`
- Error: logical-form mismatch

## test:8537:2-16815824-1

- Question: what is round1 when round3 is less than 51, total points is less than 273, round2 is less than 98 and round5 is less than 24?
- Gold: `{"sel": 2, "conds": [[4, 2, 51], [7, 2, 273], [3, 2, 98], [6, 2, 24]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 2, 51], [7, 2, 273], [3, 2, 98], [6, 2, 24]], "sel": 2}`
- Error: logical-form mismatch

## test:8539:2-16815824-1

- Question: what is round2 when round5 is more than 35, round3 is less than 51, the rank is smaller than 2 and the team is netherlands?
- Gold: `{"sel": 3, "conds": [[6, 1, 35], [4, 2, 51], [1, 0, "netherlands"], [0, 2, 2]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[6, 1, 35], [4, 2, 51], [0, 2, 2], [1, 0, "Netherlands"]], "sel": 3}`
- Error: logical-form mismatch

## test:8546:2-17583318-3

- Question: What is the premier league number when the position is forward, and the total is more than 22?
- Gold: `{"sel": 2, "conds": [[1, 0, "forward"], [6, 1, 22]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "forward"], [6, 1, 22]], "sel": 2}`
- Error: logical-form mismatch

## test:8547:2-17583318-3

- Question: What is the total when the league cup is less than 1, and the fa cup is less than 1?
- Gold: `{"sel": 6, "conds": [[4, 2, 1], [3, 2, 1]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[4, 2, 1], [3, 2, 1]], "sel": 6}`
- Error: logical-form mismatch

## test:8553:2-16566850-27

- Question: Which player lost more than 12?
- Gold: `{"sel": 4, "conds": [[2, 1, 12]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 1, 12]], "sel": 1}`
- Error: logical-form mismatch

## test:8556:2-17221632-3

- Question: How many lanes have 2 as the heat, and susanna kallur as the name?
- Gold: `{"sel": 1, "conds": [[0, 0, 2], [2, 0, "susanna kallur"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, 2], [2, 0, "susanna kallur"]], "sel": 1}`
- Error: logical-form mismatch

## test:8589:2-16605179-3

- Question: What did the Surname Lindberg rank?
- Gold: `{"sel": 0, "conds": [[1, 0, "lindberg"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Lindberg"]], "sel": 0}`
- Error: logical-form mismatch

## test:8594:2-16362719-3

- Question: How many games did team iurbentia bilbao have with rebounds higher than 212?
- Gold: `{"sel": 3, "conds": [[2, 0, "iurbentia bilbao"], [4, 1, 212]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "iurbentia bilbao"], [4, 1, 212]], "sel": 3}`
- Error: logical-form mismatch

## test:8602:2-16675572-1

- Question: what is the year when the notes is 5000 m and the competition is world junior championships in athletics?
- Gold: `{"sel": 0, "conds": [[4, 0, "5000 m"], [1, 0, "world junior championships in athletics"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "5000 m"], [1, 0, "world junior championships in athletics"]], "sel": 0}`
- Error: logical-form mismatch

## test:8637:2-1753419-2

- Question: What is the height when col is 1,077 and prominence is more than 2,349?
- Gold: `{"sel": 2, "conds": [[4, 0, "1,077"], [3, 1, "2,349"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "1,077"], [3, 1, "2,349"]], "sel": 2}`
- Error: logical-form mismatch

## test:8639:2-17607772-2

- Question: What was the result of the game after week 6 against the cleveland browns?
- Gold: `{"sel": 3, "conds": [[0, 2, 6], [2, 0, "cleveland browns"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 1, 6], [2, 0, "cleveland browns"]], "sel": 3}`
- Error: logical-form mismatch

## test:8657:2-16981801-1

- Question: WHAT IS THE WORST SCORE WHEN THE BEST SCORE WAS 8.8 AND AVERAGE WAS LARGER THAN 6.2?
- Gold: `{"sel": 4, "conds": [[3, 0, 8.8], [2, 1, 6.2]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, 8.8], [2, 1, 6.2]], "sel": 4}`
- Error: logical-form mismatch

## test:8658:2-16981801-1

- Question: WHAT IS THE TOTAL AVERAGE WITH A PLACE SMALLER THAN 1?
- Gold: `{"sel": 2, "conds": [[0, 2, 1]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 2, 1]], "sel": 2}`
- Error: logical-form mismatch

## test:8664:2-16284301-2

- Question: Who has the lowest laps with 29 points on 1 grid?
- Gold: `{"sel": 2, "conds": [[5, 0, 29], [4, 2, 1]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[5, 0, 29], [4, 0, 1]], "sel": 0}`
- Error: logical-form mismatch

## test:8681:2-16210649-4

- Question: Which Finals has a A-League of 0 6, and a Pre-Season larger than 0?
- Gold: `{"sel": 3, "conds": [[2, 0, "0 6"], [1, 1, 0]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "0 6"], [1, 1, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:8682:2-16210649-4

- Question: Which Pre-Season has a A-League of 0 1, and a Finals larger than 0?
- Gold: `{"sel": 1, "conds": [[2, 0, "0 1"], [3, 1, 0]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "0 1"], [3, 1, 0]], "sel": 1}`
- Error: logical-form mismatch

## test:8685:2-16729071-1

- Question: What is the total attendance for Candlestick Park?
- Gold: `{"sel": 6, "conds": [[4, 0, "candlestick park"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[4, 0, "Candlestick Park"]], "sel": 6}`
- Error: logical-form mismatch

## test:8702:2-17416195-6

- Question: How many goals against were scored when the points were smaller than 13, the wins were smaller than 3, and the goals for were smaller than 15?
- Gold: `{"sel": 8, "conds": [[3, 2, 13], [4, 2, 3], [7, 2, 15]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[3, 2, 13], [4, 2, 3], [7, 2, 15]], "sel": 8}`
- Error: logical-form mismatch

## test:8705:2-17416195-6

- Question: How many wins happened when there were fewer than 2 draws?
- Gold: `{"sel": 4, "conds": [[5, 2, 2]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[5, 2, 2]], "sel": 4}`
- Error: logical-form mismatch

## test:8756:2-17446978-2

- Question: How many rounds was the fight with a decision by submission (punches)?
- Gold: `{"sel": 5, "conds": [[3, 0, "submission (punches)"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "submission (punches)"]], "sel": 5}`
- Error: logical-form mismatch

## test:8796:2-16531455-4

- Question: What is the original name for the song "Sono Io"?
- Gold: `{"sel": 1, "conds": [[0, 0, "\"sono io\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Sono Io"]], "sel": 1}`
- Error: logical-form mismatch

## test:8797:2-16531455-4

- Question: Who were the singers for the song "We Rock" in French?
- Gold: `{"sel": 4, "conds": [[3, 0, "french"], [0, 0, "\"we rock\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "We Rock"], [3, 0, "French"]], "sel": 4}`
- Error: logical-form mismatch

## test:8800:2-16531455-4

- Question: Who was the singer of "This is Me" in Sweden?
- Gold: `{"sel": 4, "conds": [[1, 0, "\"this is me\""], [2, 0, "sweden"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "This Is Me"], [2, 0, "Sweden"]], "sel": 4}`
- Error: logical-form mismatch

## test:8820:2-16478687-4

- Question: Which rank had a population of 7,069,000?
- Gold: `{"sel": 0, "conds": [[2, 0, "7,069,000"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "7,069,000"]], "sel": 0}`
- Error: logical-form mismatch

## test:8821:2-16478687-4

- Question: What is the total population for the 3,616km area?
- Gold: `{"sel": 2, "conds": [[4, 0, "3,616"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[4, 0, "3,616"]], "sel": 2}`
- Error: logical-form mismatch

## test:8832:2-17323274-3

- Question: What is the total number of games that led to a record of 12-4-2 after November 22?
- Gold: `{"sel": 0, "conds": [[4, 0, "12-4-2"], [1, 1, 22]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[4, 0, "12-4-2"], [1, 1, 22]], "sel": 0}`
- Error: logical-form mismatch

## test:8853:2-17100961-19

- Question: If Notre Dame had a pick larger than 5, what's the overall pick?
- Gold: `{"sel": 2, "conds": [[5, 0, "notre dame"], [1, 1, 5]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "Notre Dame"], [1, 1, 5]], "sel": 2}`
- Error: logical-form mismatch

## test:8870:2-17396-1

- Question: When did TDB depart?
- Gold: `{"sel": 0, "conds": [[2, 0, "tdb"]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "TDB"]], "sel": 3}`
- Error: logical-form mismatch

## test:8872:2-17396-1

- Question: From how many years did tampa, FL depart?
- Gold: `{"sel": 0, "conds": [[2, 0, "tampa, fl"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "Tampa, FL"]], "sel": 0}`
- Error: logical-form mismatch

## test:8876:2-16778485-2

- Question: Which opponent was on week 2?
- Gold: `{"sel": 2, "conds": [[0, 2, 2]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 2]], "sel": 2}`
- Error: logical-form mismatch

## test:8885:2-17100961-54

- Question: WHAT PICK HAD STEVE HAMILTON IN ROUND LARGER THAN 2?
- Gold: `{"sel": 1, "conds": [[3, 0, "steve hamilton"], [0, 1, 2]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Steve Hamilton"], [0, 1, 2]], "sel": 1}`
- Error: logical-form mismatch

## test:8886:2-17100961-54

- Question: WHAT WAS THE OVERALL NUMBER WITH A POSITON OF DB, AND ROUND GREATER THAN 8?
- Gold: `{"sel": 2, "conds": [[4, 0, "db"], [0, 1, 8]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "DB"], [0, 1, 8]], "sel": 2}`
- Error: logical-form mismatch

## test:8893:2-17231302-7

- Question: How much was paid to Andy North when he placed t10?
- Gold: `{"sel": 5, "conds": [[0, 0, "t10"], [1, 0, "andy north"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Andy North"], [0, 0, "t10"]], "sel": 5}`
- Error: logical-form mismatch

## test:8895:2-17077948-1

- Question: What is the number of goals when the position is DF, the nationality is England, and the Crewe Alexandra career is 1948–1951?
- Gold: `{"sel": 5, "conds": [[2, 0, "df"], [1, 0, "england"], [3, 0, "1948–1951"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "DF"], [1, 0, "England"], [3, 0, "1948–1951"]], "sel": 5}`
- Error: logical-form mismatch

## test:8897:2-17077948-1

- Question: What is the total number of Goals with a nationality of England, and position of DF, and a Crewe Alexandra career is 1958–1962, and less than 170 appearances?
- Gold: `{"sel": 5, "conds": [[1, 0, "england"], [2, 0, "df"], [3, 0, "1958–1962"], [4, 2, 170]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "England"], [2, 0, "DF"], [3, 0, "1958–1962"], [4, 2, 170]], "sel": 5}`
- Error: logical-form mismatch

## test:8911:2-16225725-4

- Question: What is Viewers, when Episode is "A Family Affair"?
- Gold: `{"sel": 6, "conds": [[0, 0, "\"a family affair\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "A Family Affair"]], "sel": 6}`
- Error: logical-form mismatch

## test:8912:2-16225725-4

- Question: What is the lowest Share, when Episode is "Farmer Picks A Wife"?
- Gold: `{"sel": 4, "conds": [[0, 0, "\"farmer picks a wife\""]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[0, 0, "Farmer Picks a Wife"]], "sel": 4}`
- Error: logical-form mismatch

## test:8914:2-1708050-1

- Question: How many times did the team with an average start of 18.9 make the top 10?
- Gold: `{"sel": 4, "conds": [[6, 0, 18.9]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[6, 0, 18.9]], "sel": 4}`
- Error: logical-form mismatch

## test:8982:2-16388478-2

- Question: What were the Away team Kangaroos Crowd totals?
- Gold: `{"sel": 5, "conds": [[2, 0, "kangaroos"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Kangaroos"]], "sel": 5}`
- Error: logical-form mismatch

## test:8996:2-16489766-2

- Question: What is the urban population for the city of Fuzhou?
- Gold: `{"sel": 4, "conds": [[0, 0, "fuzhou"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Fuzhou"]], "sel": 4}`
- Error: logical-form mismatch

## test:8998:2-1726637-1

- Question: What is the area (in km2) for theewaterskloof, whose population in 2011 was less than 108,790?
- Gold: `{"sel": 3, "conds": [[0, 0, "theewaterskloof"], [2, 2, "108,790"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Theewaterskloof"], [2, 2, 108790]], "sel": 3}`
- Error: logical-form mismatch

## test:8999:2-1726637-1

- Question: What is the area in km2 for Cape Agulhas, whose density is larger than 9.4 inhabitants/km2 and whose population in 2011 was less than 33,038?
- Gold: `{"sel": 3, "conds": [[4, 1, 9.4], [0, 0, "cape agulhas"], [2, 2, "33,038"]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Cape Agulhas"], [4, 1, 9.4], [2, 2, "33,038"]], "sel": 3}`
- Error: logical-form mismatch

## test:9000:2-1726637-1

- Question: What is the area in km2 for the community that had a population in 2011 larger than 35,916 and a density of less than 47.1 inhabitants/km 2?
- Gold: `{"sel": 3, "conds": [[2, 1, "35,916"], [4, 2, 47.1]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 1, "35,916"], [4, 2, 47.1]], "sel": 3}`
- Error: logical-form mismatch

## test:9005:2-171361-2

- Question: What's the population of durham parish?
- Gold: `{"sel": 3, "conds": [[0, 0, "durham"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Durham"]], "sel": 3}`
- Error: logical-form mismatch

## test:9006:2-171361-2

- Question: What's the total area in kilometers of the parish addington?
- Gold: `{"sel": 2, "conds": [[0, 0, "addington"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "addington"]], "sel": 2}`
- Error: logical-form mismatch

## test:9017:2-17100961-23

- Question: What is the sum number of round with Nebraska as the college and the overall greater than 40?
- Gold: `{"sel": 0, "conds": [[5, 0, "nebraska"], [2, 1, 40]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[5, 0, "Nebraska"], [2, 1, 40]], "sel": 0}`
- Error: logical-form mismatch

## test:9031:2-16514667-5

- Question: What is the Money of the T4 Place Player with a Score of 71-66-74-67=278?
- Gold: `{"sel": 5, "conds": [[0, 0, "t4"], [3, 0, "71-66-74-67=278"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "T4"], [3, 0, "71-66-74-67=278"]], "sel": 5}`
- Error: logical-form mismatch

## test:9032:2-16514667-5

- Question: What is the Money of the Player with a Score of 71-66-74-67=278?
- Gold: `{"sel": 5, "conds": [[3, 0, "71-66-74-67=278"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "71-66-74-67=278"]], "sel": 5}`
- Error: logical-form mismatch

## test:9048:2-1751142-2

- Question: What is the total Cumulative Distance in meters that has fewer than 8 shuttles and fewer than 7 cumulative shuttles?
- Gold: `{"sel": 7, "conds": [[1, 2, 8], [2, 2, 7]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 2, 8], [2, 2, 7]], "sel": 7}`
- Error: logical-form mismatch

## test:9052:2-16713759-18

- Question: What was the aveg/g for the qb with the Att-Cmp-Int of 117–215–6?
- Gold: `{"sel": 4, "conds": [[3, 0, "117–215–6"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "117–215–6"]], "sel": 4}`
- Error: logical-form mismatch

## test:9053:2-16713759-18

- Question: What was the total effic for the quarterbacks?
- Gold: `{"sel": 2, "conds": [[0, 0, "total"]], "agg": 2}`
- Prediction: `{"agg": 4, "conds": [], "sel": 2}`
- Error: logical-form mismatch

## test:9056:2-1672976-4

- Question: What is the name of the Big Ten team who played ACC Team Maryland where 17,472 attended the game?
- Gold: `{"sel": 3, "conds": [[6, 1, "17,472"], [2, 0, "maryland"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Maryland"], [6, 0, "17,472"]], "sel": 3}`
- Error: logical-form mismatch

## test:9092:2-16645-1

- Question: What was the rural % where the source estimate was census and the urban % was larger than 57?
- Gold: `{"sel": 2, "conds": [[4, 0, "estimate"], [3, 1, 57]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "census"], [3, 1, 57]], "sel": 2}`
- Error: logical-form mismatch

## test:9112:2-17311408-7

- Question: How many games had Montreal Canadiens as an opponent?
- Gold: `{"sel": 0, "conds": [[2, 0, "montreal canadiens"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "Montreal Canadiens"]], "sel": 0}`
- Error: logical-form mismatch

## test:9130:2-16823208-3

- Question: Which Votes has a Governorate of hewler?
- Gold: `{"sel": 4, "conds": [[3, 0, "hewler"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Hewler"]], "sel": 4}`
- Error: logical-form mismatch

## test:9138:2-16750938-1

- Question: What is the Length, when the Title is "The Way To Your Heart"?
- Gold: `{"sel": 4, "conds": [[0, 0, "\"the way to your heart\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "The Way To Your Heart"]], "sel": 4}`
- Error: logical-form mismatch

## test:9184:2-16697344-2

- Question: In what year was Luxembourg Host?
- Gold: `{"sel": 0, "conds": [[1, 0, "luxembourg"]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Luxembourg"]], "sel": 0}`
- Error: logical-form mismatch

## test:9188:2-1747960-3

- Question: How many medals under total when silver is less than 2, gold is 3, and bronze is less than 0?
- Gold: `{"sel": 4, "conds": [[2, 2, 2], [1, 0, 3], [3, 2, 0]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 2, 2], [1, 0, 3], [3, 2, 0]], "sel": 4}`
- Error: logical-form mismatch

## test:9190:2-1747960-3

- Question: What is the total rank where the total is less than 5, and bronze is less than 0?
- Gold: `{"sel": 0, "conds": [[4, 2, 5], [3, 2, 0]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[4, 2, 5], [3, 2, 0]], "sel": 0}`
- Error: logical-form mismatch

## test:9205:2-16312746-2

- Question: Name the Home team of tranmere rovers?
- Gold: `{"sel": 4, "conds": [[1, 0, "tranmere rovers"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "tranmere rovers"]], "sel": 1}`
- Error: logical-form mismatch

## test:9271:2-171222-1

- Question: What is the area (in km2) for the community that has a status of village, a census ranking of 2,471 of 5,008, and a population of less than 748?
- Gold: `{"sel": 2, "conds": [[1, 0, "village"], [4, 0, "2,471 of 5,008"], [3, 2, 748]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "village"], [4, 0, "2,471 of 5,008"], [3, 2, 748]], "sel": 2}`
- Error: logical-form mismatch

## test:9273:2-171222-1

- Question: What is the area (in km2) for the village of Paquetville, with a population over 706?
- Gold: `{"sel": 2, "conds": [[1, 0, "village"], [0, 0, "paquetville"], [3, 1, 706]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Paquetville"], [3, 1, 706]], "sel": 2}`
- Error: logical-form mismatch

## test:9274:2-171222-1

- Question: What is the area (in km2) for the town of lamèque, with a population of less than 4,351?
- Gold: `{"sel": 2, "conds": [[1, 0, "town"], [3, 2, "4,351"], [0, 0, "lamèque"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Lamèque"], [3, 2, 4351]], "sel": 2}`
- Error: logical-form mismatch

## test:9286:2-169523-2

- Question: Round 3 with less than 54 for Round 4?
- Gold: `{"sel": 3, "conds": [[4, 0, "54"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 2, 54]], "sel": 3}`
- Error: logical-form mismatch

## test:9326:2-169719-4

- Question: How much Gold has a Silver smaller than 3, and a Total of 9, and a Bronze smaller than 1?
- Gold: `{"sel": 2, "conds": [[3, 2, 3], [5, 0, 9], [4, 2, 1]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[3, 2, 3], [5, 0, 9], [4, 2, 1]], "sel": 2}`
- Error: logical-form mismatch

## test:9327:2-169719-4

- Question: How much Gold has a Silver smaller than 14, and a Rank larger than 8, and a Bronze of 3?
- Gold: `{"sel": 2, "conds": [[3, 2, 14], [0, 1, 8], [4, 0, 3]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 2, 14], [0, 1, 8], [4, 0, 3]], "sel": 2}`
- Error: logical-form mismatch

## test:9328:2-169719-4

- Question: How much Bronze has a Silver larger than 2, and a Nation of mixed team, and a Rank larger than 4?
- Gold: `{"sel": 4, "conds": [[3, 1, 2], [1, 0, "mixed team"], [0, 1, 4]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 1, 2], [1, 0, "mixed team"], [0, 1, 4]], "sel": 4}`
- Error: logical-form mismatch

## test:9333:2-16677972-2

- Question: What's the total attendance of games against the New York Giants after week 13?
- Gold: `{"sel": 4, "conds": [[0, 1, 13], [2, 0, "new york giants"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 1, 13], [2, 0, "New York Giants"]], "sel": 4}`
- Error: logical-form mismatch

## test:9358:2-165470-1

- Question: Which Total population (2010 census) has an Area (km 2) smaller than 147,307.00?
- Gold: `{"sel": 4, "conds": [[1, 2, "147,307.00"]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[1, 2, "147,307.00"]], "sel": 4}`
- Error: logical-form mismatch

## test:9359:2-165470-1

- Question: Which Total population (2005 estimate) has a Total population (2010 census) of 3,626,119?
- Gold: `{"sel": 3, "conds": [[4, 0, "3,626,119"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "3,626,119"]], "sel": 3}`
- Error: logical-form mismatch

## test:9360:2-165470-1

- Question: Which Total population (2005 estimate) has a Province of west kalimantan (kalimantan barat), and an Area (km 2) smaller than 147,307.00?
- Gold: `{"sel": 3, "conds": [[0, 0, "west kalimantan (kalimantan barat)"], [1, 2, "147,307.00"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "west kalimantan (kalimantan barat)"], [1, 2, "147,307.00"]], "sel": 3}`
- Error: logical-form mismatch

## test:9376:2-16590039-1

- Question: What was the Lead for the 2009 WCC when Wang Bingyu news was the skip?
- Gold: `{"sel": 2, "conds": [[1, 0, "wang bingyu"], [0, 0, "2009 wcc"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "2009 WCC"], [1, 0, "Wang Bingyu news"]], "sel": 2}`
- Error: logical-form mismatch

## test:9398:2-1698244-4

- Question: What is the total number of top fives in 2010 when casey mears had more than 0 wins?
- Gold: `{"sel": 3, "conds": [[0, 0, "2010"], [2, 1, 0]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "2010"], [2, 1, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:9400:2-1698244-4

- Question: What is the total number of top fives when casey mears had more than 1 poles and top tens less than 9?
- Gold: `{"sel": 3, "conds": [[5, 1, 1], [4, 2, 9]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[5, 1, 1], [4, 2, 9]], "sel": 3}`
- Error: logical-form mismatch

## test:9404:2-17129548-3

- Question: Which Score has a Place of t1, and a Player of scott simpson?
- Gold: `{"sel": 3, "conds": [[0, 0, "t1"], [1, 0, "scott simpson"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "t1"], [1, 0, "scott simpson"]], "sel": 3}`
- Error: logical-form mismatch

## test:9406:2-17355628-6

- Question: How many games were on December 5?
- Gold: `{"sel": 0, "conds": [[1, 0, "december 5"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "December 5"]], "sel": 0}`
- Error: logical-form mismatch

## test:9419:2-17205115-1

- Question: How many division titles does the team with 23 playoff appearances and more than 1 conference titles have?
- Gold: `{"sel": 7, "conds": [[4, 0, 23], [8, 1, 1]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[4, 0, 23], [8, 1, 1]], "sel": 7}`
- Error: logical-form mismatch

## test:9421:2-16864968-9

- Question: What hame has points larger than 81?
- Gold: `{"sel": 0, "conds": [[7, 1, 81]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[7, 1, 81]], "sel": 0}`
- Error: logical-form mismatch

## test:9427:2-17201869-9

- Question: How many matches did Carlos Kameni play in, who had an average larger than 1.27?
- Gold: `{"sel": 2, "conds": [[0, 0, "carlos kameni"], [3, 1, 1.27]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Carlos Kameni"], [3, 1, 1.27]], "sel": 2}`
- Error: logical-form mismatch

## test:9430:2-17437287-2

- Question: What is the number of ties when Altrincham is the home team?
- Gold: `{"sel": 0, "conds": [[1, 0, "altrincham"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "Altrincham"]], "sel": 0}`
- Error: logical-form mismatch

## test:9436:2-17510803-1

- Question: How many rounds were played in the matching resulting in a Points For score of 343?
- Gold: `{"sel": 1, "conds": [[4, 0, "343"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "343"]], "sel": 1}`
- Error: logical-form mismatch

## test:9438:2-16990777-3

- Question: What is the church made from in Hamburg?
- Gold: `{"sel": 5, "conds": [[4, 0, "church"], [2, 0, "hamburg"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Hamburg"]], "sel": 0}`
- Error: logical-form mismatch

## test:9442:2-17064691-1

- Question: What is the pick for the Maryland-Eastern Shore team with a round lower than 2?
- Gold: `{"sel": 1, "conds": [[5, 0, "maryland-eastern shore"], [0, 2, 2]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "Maryland-Eastern Shore"], [0, 2, 2]], "sel": 1}`
- Error: logical-form mismatch

## test:9447:2-17064691-1

- Question: What is the pick for Mickey Johnson with fewer than 4 rounds?
- Gold: `{"sel": 1, "conds": [[2, 0, "mickey johnson"], [0, 2, 4]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Mickey Johnson"], [0, 2, 4]], "sel": 1}`
- Error: logical-form mismatch

## test:9461:2-16644252-2

- Question: What is the total number for the week with a record of 0-11?
- Gold: `{"sel": 0, "conds": [[6, 0, "0-11"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[6, 0, "0-11"]], "sel": 0}`
- Error: logical-form mismatch

## test:9463:2-16644252-2

- Question: What is the total number for the week that has lions' points of 27, and an opponents' points of 24?
- Gold: `{"sel": 0, "conds": [[4, 0, "27"], [5, 0, "24"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[4, 0, "27"], [5, 0, "24"]], "sel": 0}`
- Error: logical-form mismatch

## test:9493:2-17419587-1

- Question: What is the sum of 2010-11 when the rank is greater than 11?
- Gold: `{"sel": 11, "conds": [[0, 1, 11]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 1, 11]], "sel": 11}`
- Error: logical-form mismatch

## test:9505:2-1730288-3

- Question: What is the sum of against scores when there are 3 losses and less than 6 games played?
- Gold: `{"sel": 4, "conds": [[3, 0, 3], [1, 2, 6]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[3, 0, 3], [1, 2, 6]], "sel": 4}`
- Error: logical-form mismatch

## test:9507:2-16669773-1

- Question: What was the sample size for the poll from Nov 9-11, 2007 with a margin of error less than 4.3?
- Gold: `{"sel": 1, "conds": [[3, 0, "nov 9-11, 2007"], [2, 2, 4.3]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Nov 9-11, 2007"], [2, 2, 4.3]], "sel": 1}`
- Error: logical-form mismatch

## test:9514:2-175442-1

- Question: What is the length of the Panther Chameleon?
- Gold: `{"sel": 3, "conds": [[1, 0, "panther chameleon"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Panther Chameleon"]], "sel": 2}`
- Error: logical-form mismatch

## test:9528:2-163231-4

- Question: How many totals have golds of 3, silvers of 3, and bronzes under 3?
- Gold: `{"sel": 5, "conds": [[2, 0, "3"], [4, 2, 3], [3, 0, "3"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "3"], [3, 0, "3"], [4, 2, 3]], "sel": 5}`
- Error: logical-form mismatch

## test:9552:2-16457056-1

- Question: How much is the money ($) when the country is united states, to par is e and the score is 72-75-70-71=288?
- Gold: `{"sel": 5, "conds": [[2, 0, "united states"], [4, 0, "e"], [3, 0, "72-75-70-71=288"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "united states"], [4, 0, "e"], [3, 0, "72-75-70-71=288"]], "sel": 5}`
- Error: logical-form mismatch

## test:9554:2-16457056-1

- Question: How much is the money ($) when the score is 67-71-72-72=282?
- Gold: `{"sel": 5, "conds": [[3, 0, "67-71-72-72=282"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "67-71-72-72=282"]], "sel": 5}`
- Error: logical-form mismatch

## test:9588:2-17270998-1

- Question: How many points were scored by a car that led for 0 laps and started in grid 10?
- Gold: `{"sel": 8, "conds": [[7, 0, "0"], [6, 0, "10"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[7, 0, "0"], [6, 0, "10"]], "sel": 8}`
- Error: logical-form mismatch

## test:9590:2-16226584-1

- Question: What is the total number of Length Feet, when Parish is Clarendon, when Km From Kingston is 71.2, and when Length Meters is less than 21.3?
- Gold: `{"sel": 4, "conds": [[3, 0, "clarendon"], [2, 0, 71.2], [5, 2, 21.3]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[3, 0, "Clarendon"], [2, 0, 71.2], [5, 2, 21.3]], "sel": 4}`
- Error: logical-form mismatch

## test:9597:2-17433696-2

- Question: How many rounds was the fight at UFC 34?
- Gold: `{"sel": 5, "conds": [[4, 0, "ufc 34"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "UFC 34"]], "sel": 5}`
- Error: logical-form mismatch

## test:9633:2-17323777-1

- Question: What is the total number for the pick of the player Wayne Fowler and a round after 7?
- Gold: `{"sel": 1, "conds": [[2, 0, "wayne fowler"], [0, 1, 7]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[2, 0, "Wayne Fowler"], [0, 1, 7]], "sel": 1}`
- Error: logical-form mismatch

## test:9646:2-17589865-2

- Question: What is the number of people in attendance when venue shows A, and Di Matteo, M. Hughes were the scorers?
- Gold: `{"sel": 5, "conds": [[3, 0, "a"], [6, 0, "di matteo, m. hughes"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "A"], [6, 0, "Di Matteo , M. Hughes"]], "sel": 5}`
- Error: logical-form mismatch

## test:9652:2-170916-2

- Question: WHAT IS THE ENROLLMENT FOR école saint-therèse AFTER 1954?
- Gold: `{"sel": 4, "conds": [[0, 0, "école saint-therèse"], [3, 1, 1954]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "école saint-therèse"], [3, 1, 1954]], "sel": 4}`
- Error: logical-form mismatch

## test:9654:2-16458346-3

- Question: Where is Miller Barber from?
- Gold: `{"sel": 0, "conds": [[1, 0, "miller barber"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Miller Barber"]], "sel": 2}`
- Error: logical-form mismatch

## test:9667:2-1646586-4

- Question: With a Morse Taper number less than 3 and a C (max) of 59.5 what is the total of D (max)?
- Gold: `{"sel": 4, "conds": [[0, 2, 3], [3, 0, 59.5]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 2, 3], [3, 0, 59.5]], "sel": 4}`
- Error: logical-form mismatch

## test:9712:2-17131208-2

- Question: How many weeks have a Date of december 4, 1976, and an Attendance larger than 57,366?
- Gold: `{"sel": 0, "conds": [[1, 0, "december 4, 1976"], [4, 1, "57,366"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "december 4, 1976"], [4, 1, "57,366"]], "sel": 0}`
- Error: logical-form mismatch

## test:9713:2-17419587-2

- Question: What was the total number of aircrafts in 2011 for sydney airport that was ranked number 1?
- Gold: `{"sel": 3, "conds": [[1, 0, "sydney airport"], [0, 2, 1]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "sydney airport"], [0, 0, 1]], "sel": 3}`
- Error: logical-form mismatch

## test:9717:2-16882078-2

- Question: What is the result for week 12 against the Green Bay Packers?
- Gold: `{"sel": 3, "conds": [[0, 1, 12], [2, 0, "green bay packers"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 12], [2, 0, "Green Bay Packers"]], "sel": 3}`
- Error: logical-form mismatch

## test:9720:2-1637981-7

- Question: For how many years did Detroit have a passenger fare of $307.29?
- Gold: `{"sel": 0, "conds": [[2, 0, "$307.29"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "$307.29"]], "sel": 0}`
- Error: logical-form mismatch

## test:9726:2-16454472-14

- Question: Which League Cup goals have a Scorer of ken houghton, and an FA Cup goals smaller than 0?
- Gold: `{"sel": 4, "conds": [[0, 0, "ken houghton"], [3, 2, 0]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "ken houghton"], [3, 2, 0]], "sel": 4}`
- Error: logical-form mismatch

## test:9741:2-17012578-6

- Question: How many ends lost for Alberta when stolen ends are greater than 7?
- Gold: `{"sel": 3, "conds": [[0, 0, "alberta"], [5, 1, 7]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Alberta"], [5, 1, 7]], "sel": 3}`
- Error: logical-form mismatch

## test:9795:2-17386087-2

- Question: What was the attendance at the game before week 8, held on October 25, 1981?
- Gold: `{"sel": 4, "conds": [[1, 0, "october 25, 1981"], [0, 2, 8]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 2, 8], [1, 0, "October 25, 1981"]], "sel": 4}`
- Error: logical-form mismatch

## test:9807:2-16998383-1

- Question: WHAT IS THE ELEVATION OF THE UNAKA MOUNTAINS, IN ROAN HIGH BLUFF PEAK, AND ISOLATION LARGER THAN 1.54?
- Gold: `{"sel": 2, "conds": [[3, 0, "unaka mountains"], [1, 0, "roan high bluff"], [4, 1, 1.54]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Unaka Mountains"], [1, 0, "Roan High Bluff"], [4, 1, 1.54]], "sel": 2}`
- Error: logical-form mismatch

## test:9809:2-16678524-2

- Question: What was the Attendance on Week 8?
- Gold: `{"sel": 4, "conds": [[0, 0, 8]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 8]], "sel": 4}`
- Error: logical-form mismatch

## test:9846:2-17271053-2

- Question: What is the number of laps of the grid larger than 22 with a +1:29.001 time?
- Gold: `{"sel": 2, "conds": [[4, 1, 22], [3, 0, "+1:29.001"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 1, 22], [3, 0, "+1:29.001"]], "sel": 2}`
- Error: logical-form mismatch

## test:9849:2-17565113-2

- Question: What is the maximum 2002 figure when 2008 is 19.5, 2006 is less than 24.5 and 1999 is 18.3?
- Gold: `{"sel": 4, "conds": [[10, 1, 19.5], [8, 2, 24.5], [1, 0, 18.3]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[10, 0, 19.5], [8, 2, 24.5], [1, 0, 18.3]], "sel": 4}`
- Error: logical-form mismatch

## test:9852:2-17565113-2

- Question: What is the 2010 figure for the district of Columbia where the 2004 figure is more than 12.3?
- Gold: `{"sel": 12, "conds": [[0, 0, "district of columbia"], [6, 1, 12.3]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "District of Columbia"], [6, 1, 12.3]], "sel": 12}`
- Error: logical-form mismatch

## test:9888:2-16642822-1

- Question: How much tonnage was damaged?
- Gold: `{"sel": 3, "conds": [[4, 0, "damaged"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "damaged"]], "sel": 3}`
- Error: logical-form mismatch

## test:9917:2-17054062-2

- Question: What was the date of appointment for Christos Kassianos who belonged to AEK?
- Gold: `{"sel": 5, "conds": [[0, 0, "aek"], [4, 0, "christos kassianos"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Christos Kassianos"], [0, 0, "AEK"]], "sel": 5}`
- Error: logical-form mismatch

## test:9923:2-16902902-1

- Question: What is the sum of complement commander Valkenburg received?
- Gold: `{"sel": 3, "conds": [[2, 0, "valkenburg"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[2, 0, "Valkenburg"]], "sel": 3}`
- Error: logical-form mismatch

## test:9940:2-1639167-1

- Question: How many sprint points have 0 extra laps for rank 19?
- Gold: `{"sel": 2, "conds": [[3, 0, "0"], [0, 0, "19"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, 0], [0, 0, 19]], "sel": 2}`
- Error: logical-form mismatch

## test:9941:2-1639167-1

- Question: How many sprint points contribute to 2 total points?
- Gold: `{"sel": 2, "conds": [[4, 0, "2"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 0, 2]], "sel": 2}`
- Error: logical-form mismatch

## test:9943:2-1639167-1

- Question: What is the number of extra laps for 9 total points?
- Gold: `{"sel": 3, "conds": [[4, 0, "9"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 0, 9]], "sel": 3}`
- Error: logical-form mismatch

## test:9956:2-169574-1

- Question: Who has the title and rank 14, and a worldwide gross of $202,292,902?
- Gold: `{"sel": 1, "conds": [[0, 1, 14], [4, 0, "$202,292,902"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 14], [4, 0, "$202,292,902"]], "sel": 1}`
- Error: logical-form mismatch

## test:9969:2-17104192-3

- Question: what is the silver when the nation is japan and the total is less than 1?
- Gold: `{"sel": 3, "conds": [[1, 0, "japan"], [5, 2, 1]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "japan"], [5, 2, 1]], "sel": 3}`
- Error: logical-form mismatch

## test:9970:2-17104192-3

- Question: what is the bronze when silver is 1, gold is 0 the rank is 11 and the total is more than 1?
- Gold: `{"sel": 4, "conds": [[3, 0, 1], [2, 0, 0], [0, 0, "11"], [5, 1, 1]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[3, 0, 1], [2, 0, 0], [0, 0, 11], [5, 1, 1]], "sel": 4}`
- Error: logical-form mismatch

## test:9989:2-17010918-3

- Question: How many Silver medals for the Nation of Turkey with a Total of less than 2?
- Gold: `{"sel": 3, "conds": [[1, 0, "turkey"], [5, 2, 2]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Turkey"], [5, 2, 2]], "sel": 3}`
- Error: logical-form mismatch

## test:9990:2-17010918-3

- Question: How many Gold for the Nation in Rank 15 with 0 Silver?
- Gold: `{"sel": 2, "conds": [[0, 0, "15"], [3, 1, 0]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "15"], [3, 0, 0]], "sel": 2}`
- Error: logical-form mismatch

## test:9991:2-1720632-1

- Question: WHAT IS THE TOTAL NUMBER WITH A WARD SMALLER THAN 0?
- Gold: `{"sel": 3, "conds": [[1, 2, 0]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 2, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:10018:2-17573582-1

- Question: What year was the composition by Mejo Joseph?
- Gold: `{"sel": 0, "conds": [[3, 0, "mejo joseph"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Mejo Joseph"]], "sel": 0}`
- Error: logical-form mismatch

## test:10065:2-17543955-1

- Question: What is the number for match when the draws in more than 0, the team is Polonia Bydgoszcz, and there are less than 17 points?
- Gold: `{"sel": 1, "conds": [[3, 1, 0], [0, 0, "polonia bydgoszcz"], [2, 2, 17]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[3, 1, 0], [0, 0, "Polonia Bydgoszcz"], [2, 2, 17]], "sel": 1}`
- Error: logical-form mismatch

## test:10071:2-17596418-6

- Question: what is the goals when the country is wal, the name is smith and apps is more than 0?
- Gold: `{"sel": 5, "conds": [[1, 0, "wal"], [0, 0, "smith"], [4, 1, 0]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "wal"], [0, 0, "smith"], [4, 1, 0]], "sel": 5}`
- Error: logical-form mismatch

## test:10108:2-16744814-2

- Question: How many silver medals did the team that had 5 bronze and less than 16 gold have?
- Gold: `{"sel": 2, "conds": [[3, 1, 5], [1, 2, 16]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[3, 0, 5], [1, 2, 16]], "sel": 2}`
- Error: logical-form mismatch

## test:10124:2-10869537-3

- Question: When the Away team scored 20.15 (135) on the Date of 23 april 1973, how many people were in the crowd?
- Gold: `{"sel": 5, "conds": [[6, 0, "23 april 1973"], [3, 0, "20.15 (135)"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "20.15 (135)"], [6, 0, "23 april 1973"]], "sel": 5}`
- Error: logical-form mismatch

## test:10130:2-1161065-28

- Question: What is the lowest when the total is 353,069 and average is larger than 47,425?
- Gold: `{"sel": 4, "conds": [[5, 2, "353,069"], [2, 1, "47,425"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "353,069"], [2, 1, "47,425"]], "sel": 4}`
- Error: logical-form mismatch

## test:10135:2-10790397-3

- Question: Which home team had a crowd size of 14,000 at Junction Oval?
- Gold: `{"sel": 0, "conds": [[5, 1, "14,000"], [4, 0, "junction oval"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "14,000"], [4, 0, "Junction Oval"]], "sel": 0}`
- Error: logical-form mismatch

## test:10140:2-11108194-2

- Question: Which TV network is a spanish commercial network with greater than 53,674,000 households viewable and place lower than 1?
- Gold: `{"sel": 1, "conds": [[4, 0, "spanish commercial"], [3, 1, "53,674,000"], [0, 1, 1]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "spanish commercial"], [3, 1, 53674000], [0, 2, 1]], "sel": 1}`
- Error: logical-form mismatch

## test:10157:2-10809368-1

- Question: How many people were in the crowd for a game than had carlton as the visiting team?
- Gold: `{"sel": 5, "conds": [[2, 0, "carlton"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "carlton"]], "sel": 5}`
- Error: logical-form mismatch

## test:10229:2-10809823-10

- Question: What is the crowd with Away team of hawthorn?
- Gold: `{"sel": 5, "conds": [[2, 0, "hawthorn"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "hawthorn"]], "sel": 5}`
- Error: logical-form mismatch

## test:10240:2-11750987-1

- Question: What is the Gaelic Football Stadium at McHale Park's ranking in total capacity?
- Gold: `{"sel": 0, "conds": [[1, 0, "mchale park"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "McHale Park"]], "sel": 0}`
- Error: logical-form mismatch

## test:10257:2-10887680-22

- Question: How many spectators at the game with a home team score of 16.15 (111)?
- Gold: `{"sel": 5, "conds": [[1, 0, "16.15 (111)"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "16.15 (111)"]], "sel": 5}`
- Error: logical-form mismatch

## test:10281:2-10806852-15

- Question: What was the away team at collingwood?
- Gold: `{"sel": 3, "conds": [[0, 0, "collingwood"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "collingwood"]], "sel": 2}`
- Error: logical-form mismatch

## test:10283:2-11207040-5

- Question: What is the greatest capacity when the largest number in attendance is 6,192?
- Gold: `{"sel": 2, "conds": [[3, 1, "6,192"]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[3, 0, "6,192"]], "sel": 2}`
- Error: logical-form mismatch

## test:10284:2-11207040-5

- Question: What is the total number for smallest number in attendance at Broadwood Stadium when the largest attendance was 6,192, with an average of 2,468?
- Gold: `{"sel": 4, "conds": [[3, 2, "6,192"], [5, 2, "2,468"], [1, 0, "broadwood stadium"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "Broadwood Stadium"], [3, 0, "6,192"], [5, 0, "2,468"]], "sel": 4}`
- Error: logical-form mismatch

## test:10298:2-11173438-1

- Question: What was the attendance on November 1, 1942?
- Gold: `{"sel": 4, "conds": [[1, 0, "november 1, 1942"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "november 1, 1942"]], "sel": 4}`
- Error: logical-form mismatch

## test:10319:2-1123403-2

- Question: What is the highest grid when the race was retired due to the gearbox after 67 laps?
- Gold: `{"sel": 4, "conds": [[3, 0, "gearbox"], [2, 1, 67]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[3, 0, "Gearbox"], [2, 0, 67]], "sel": 4}`
- Error: logical-form mismatch

## test:10321:2-1123403-2

- Question: How many laps did Nick Heidfeld drive on grids larger than 4?
- Gold: `{"sel": 2, "conds": [[4, 1, 4], [0, 0, "nick heidfeld"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Nick Heidfeld"], [4, 1, 4]], "sel": 2}`
- Error: logical-form mismatch

## test:10322:2-11051308-1

- Question: What is the full number of New Council when the previous council was 54 and the staying councilor number is bigger than 36?
- Gold: `{"sel": 5, "conds": [[1, 0, 54], [2, 1, 36]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, 54], [2, 1, 36]], "sel": 5}`
- Error: logical-form mismatch

## test:10323:2-11051308-1

- Question: Which number of New Councils had a previous council number of 19 and the seats up for election were bigger than 6?
- Gold: `{"sel": 5, "conds": [[1, 0, 19], [3, 2, 6]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, 19], [3, 1, 6]], "sel": 5}`
- Error: logical-form mismatch

## test:10325:2-11201709-1

- Question: What is the number of points for the vehicle with a mp4-17d chassis earlier than 2003?
- Gold: `{"sel": 4, "conds": [[1, 0, "mp4-17d"], [0, 2, 2003]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "mp4-17d"], [0, 2, 2003]], "sel": 4}`
- Error: logical-form mismatch

## test:10336:2-10885968-21

- Question: How big was the crowd of the away team that scored 18.16 (124)?
- Gold: `{"sel": 5, "conds": [[3, 0, "18.16 (124)"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "18.16 (124)"]], "sel": 5}`
- Error: logical-form mismatch

## test:10347:2-1139835-5

- Question: Who won the season of 1998?
- Gold: `{"sel": 7, "conds": [[0, 0, 1998]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 1998]], "sel": 1}`
- Error: logical-form mismatch

## test:10357:2-1081759-3

- Question: For a vehicle below 25 feet, that was retired in 2005 and had a navistar t444e engine, what was the total width?
- Gold: `{"sel": 3, "conds": [[4, 0, "navistar t444e"], [6, 0, "2005"], [2, 2, 25]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[2, 2, 25], [6, 0, "2005"], [4, 0, "navistar t444e"]], "sel": 3}`
- Error: logical-form mismatch

## test:10360:2-11902366-3

- Question: What is the number of people in attendance when the decision was brodeur and the home was ottawa?
- Gold: `{"sel": 5, "conds": [[4, 0, "brodeur"], [3, 0, "ottawa"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "brodeur"], [3, 0, "ottawa"]], "sel": 5}`
- Error: logical-form mismatch

## test:10379:2-10809142-3

- Question: What is the crowd with Home team score of 16.9 (105)?
- Gold: `{"sel": 5, "conds": [[1, 0, "16.9 (105)"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "16.9 (105)"]], "sel": 5}`
- Error: logical-form mismatch

## test:10382:2-11204543-21

- Question: How many ties drawed at 20?
- Gold: `{"sel": 3, "conds": [[2, 0, "20"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[2, 0, 20]], "sel": 3}`
- Error: logical-form mismatch

## test:10390:2-12030247-5

- Question: How much cash on hand did a candidate with a total debt of 4,516,030 and total receipts less than 9,969,292 have?
- Gold: `{"sel": 5, "conds": [[6, 0, "4,516,030"], [1, 2, "9,969,292"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[6, 0, "4,516,030"], [1, 2, "9,969,292"]], "sel": 5}`
- Error: logical-form mismatch

## test:10400:2-11603006-4

- Question: What rank has less than 22 wins
- Gold: `{"sel": 0, "conds": [[4, 2, 22]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 2, 22]], "sel": 0}`
- Error: logical-form mismatch

## test:10409:2-10809444-18

- Question: What is the total number of people that attended the glenferrie oval venue?
- Gold: `{"sel": 5, "conds": [[4, 0, "glenferrie oval"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "glenferrie oval"]], "sel": 5}`
- Error: logical-form mismatch

## test:10428:2-1122994-1

- Question: How many Laps does Eddie Cheever have?
- Gold: `{"sel": 2, "conds": [[0, 0, "eddie cheever"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Eddie Cheever"]], "sel": 2}`
- Error: logical-form mismatch

## test:10433:2-11512253-7

- Question: How many were in attendance for the loss of rekar (4–5)?
- Gold: `{"sel": 4, "conds": [[3, 0, "rekar (4–5)"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "Rekar (4–5)"]], "sel": 4}`
- Error: logical-form mismatch

## test:10456:2-1123533-1

- Question: What is the total number of laps where time/retired is +2 laps and the grid number is bigger than 18?
- Gold: `{"sel": 2, "conds": [[3, 0, "+2 laps"], [4, 1, 18]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "+2 laps"], [4, 1, 18]], "sel": 2}`
- Error: logical-form mismatch

## test:10478:2-11964379-6

- Question: How many people attended the match on 1/11?
- Gold: `{"sel": 5, "conds": [[0, 0, "1/11"]], "agg": 0}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "1/11"]], "sel": 5}`
- Error: logical-form mismatch

## test:10500:2-1123326-2

- Question: how many laps was the driver jacques villeneuve and the grid more than 7?
- Gold: `{"sel": 2, "conds": [[0, 0, "jacques villeneuve"], [4, 1, 7]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "jacques villeneuve"], [4, 1, 7]], "sel": 2}`
- Error: logical-form mismatch

## test:10537:2-1104201-1

- Question: Where was the game that the attendance was 24,694?
- Gold: `{"sel": 0, "conds": [[5, 0, "24,694"]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "24,694"]], "sel": 3}`
- Error: logical-form mismatch

## test:10540:2-11718680-1

- Question: How many league cup goals for tyrone thompson with 0 FLT goals?
- Gold: `{"sel": 8, "conds": [[1, 0, "tyrone thompson"], [10, 1, 0]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "tyrone thompson"], [10, 0, 0]], "sel": 8}`
- Error: logical-form mismatch

## test:10541:2-11718680-1

- Question: How many goals for the FW with 0 FA cup appearances and over 0 playoff goals?
- Gold: `{"sel": 4, "conds": [[2, 0, "fw"], [5, 0, "0"], [12, 1, 0]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "FW"], [5, 0, "0"], [12, 1, 0]], "sel": 14}`
- Error: logical-form mismatch

## test:10545:2-11677694-12

- Question: What is total orders for goals of 239?
- Gold: `{"sel": 0, "conds": [[4, 0, 239]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[4, 0, 239]], "sel": 0}`
- Error: logical-form mismatch

## test:10555:2-11389949-1

- Question: What is the rank for the total less than 1?
- Gold: `{"sel": 0, "conds": [[5, 2, 1]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[5, 2, 1]], "sel": 0}`
- Error: logical-form mismatch

## test:10562:2-10887379-21

- Question: Who was the team with the smallest crowd at the Princes Park venue?
- Gold: `{"sel": 5, "conds": [[4, 0, "princes park"]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "princes park"]], "sel": 0}`
- Error: logical-form mismatch

## test:10563:2-10967481-1

- Question: what is the size km² when the density hab/km is 8,321?
- Gold: `{"sel": 2, "conds": [[4, 0, "8,321"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "8,321"]], "sel": 2}`
- Error: logical-form mismatch

## test:10572:2-11603116-3

- Question: What's the wins with less than 27 events and earnings of $1,579,988?
- Gold: `{"sel": 5, "conds": [[3, 0, "1,579,988"], [4, 2, 27]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 2, 27], [3, 0, "1,579,988"]], "sel": 5}`
- Error: logical-form mismatch

## test:10573:2-11603116-3

- Question: What's the total earnings ($) with more than two wins and a rank less than 2?
- Gold: `{"sel": 3, "conds": [[5, 1, 2], [0, 2, 2]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[5, 1, 2], [0, 2, 2]], "sel": 3}`
- Error: logical-form mismatch

## test:10584:2-1169552-3

- Question: How many have a class of 330?
- Gold: `{"sel": 4, "conds": [[0, 0, "330"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "330"]], "sel": 0}`
- Error: logical-form mismatch

## test:10591:2-10806592-12

- Question: Which team played away at Victoria park?
- Gold: `{"sel": 3, "conds": [[4, 0, "victoria park"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "victoria park"]], "sel": 2}`
- Error: logical-form mismatch

## test:10642:2-10883333-9

- Question: Who was the home team at the game with a crowd larger than 32,576?
- Gold: `{"sel": 1, "conds": [[5, 1, "32,576"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 1, "32,576"]], "sel": 0}`
- Error: logical-form mismatch

## test:10665:2-10790397-16

- Question: Which home team played an away team with a score of 6.4 (40)?
- Gold: `{"sel": 1, "conds": [[3, 0, "6.4 (40)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "6.4 (40)"]], "sel": 0}`
- Error: logical-form mismatch

## test:10679:2-1122413-1

- Question: What's the total grid of Bruce Mclaren?
- Gold: `{"sel": 4, "conds": [[0, 0, "bruce mclaren"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "Bruce Mclaren"]], "sel": 4}`
- Error: logical-form mismatch

## test:10696:2-1123173-2

- Question: how many laps have a time/retired of +1 lap and mark blundell is the driver?
- Gold: `{"sel": 2, "conds": [[3, 0, "+1 lap"], [0, 0, "mark blundell"]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "+1 Lap"], [0, 0, "Mark Blundell"]], "sel": 2}`
- Error: logical-form mismatch

## test:10703:2-11513625-2

- Question: What were the total games in the Big Ten conference when Nebraska lost fewer than 488 games and had a Pct less than 0.7014?
- Gold: `{"sel": 5, "conds": [[6, 0, "big ten"], [1, 2, 488], [0, 0, "nebraska"], [3, 2, 0.7014]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Nebraska"], [1, 2, 488], [3, 2, 0.7014], [6, 0, "Big Ten"]], "sel": 5}`
- Error: logical-form mismatch

## test:10704:2-11513625-2

- Question: What is Akron's highest Pct in 100 years?
- Gold: `{"sel": 3, "conds": [[4, 1, 100], [0, 0, "akron"]], "agg": 3}`
- Prediction: `{"agg": 1, "conds": [[0, 0, "Akron"], [4, 0, 100]], "sel": 3}`
- Error: logical-form mismatch

## test:10705:2-10784349-1

- Question: How many people attended the game at Lake Oval?
- Gold: `{"sel": 5, "conds": [[4, 0, "lake oval"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "lake oval"]], "sel": 5}`
- Error: logical-form mismatch

## test:10729:2-11960091-5

- Question: How many people were in attendance for the game with a score of 98–111?
- Gold: `{"sel": 5, "conds": [[2, 0, "98–111"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "98–111"]], "sel": 5}`
- Error: logical-form mismatch

## test:10738:2-10887680-4

- Question: What was the crowd size when Geelong played at home?
- Gold: `{"sel": 5, "conds": [[0, 0, "geelong"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "geelong"]], "sel": 5}`
- Error: logical-form mismatch

## test:10743:2-10790510-3

- Question: What was the score for the away team at Collingwood?
- Gold: `{"sel": 1, "conds": [[2, 0, "collingwood"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "collingwood"]], "sel": 3}`
- Error: logical-form mismatch

## test:10744:2-10790510-3

- Question: Who is the home team of South Melbourne?
- Gold: `{"sel": 2, "conds": [[0, 0, "south melbourne"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "south melbourne"]], "sel": 0}`
- Error: logical-form mismatch

## test:10751:2-11303346-2

- Question: Name the Trofeo Fast team for roberto visentini
- Gold: `{"sel": 6, "conds": [[1, 0, "roberto visentini"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "roberto visentini"]], "sel": 6}`
- Error: logical-form mismatch

## test:10780:2-1140067-1

- Question: How many rounds have a chassis of thl2?
- Gold: `{"sel": 6, "conds": [[2, 0, "thl2"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "thl2"]], "sel": 6}`
- Error: logical-form mismatch

## test:10789:2-10809368-2

- Question: In the match where the crowd was greater than 14,000 and the home team scored 15.14 (104) who was the away team?
- Gold: `{"sel": 3, "conds": [[5, 1, "14,000"], [1, 0, "15.14 (104)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 1, "14,000"], [1, 0, "15.14 (104)"]], "sel": 2}`
- Error: logical-form mismatch

## test:10790:2-1131781-1

- Question: How many goals were scored with a pos larger than 4 and active in 2001-?
- Gold: `{"sel": 2, "conds": [[0, 1, 4], [4, 0, "2001-"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 1, 4], [4, 0, "2001-"]], "sel": 2}`
- Error: logical-form mismatch

## test:10821:2-11818965-2

- Question: How many points were scored in 1:44:59.557 of time?
- Gold: `{"sel": 5, "conds": [[3, 0, "1:44:59.557"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "1:44:59.557"]], "sel": 5}`
- Error: logical-form mismatch

## test:10858:2-11789730-4

- Question: How many tournament titles for texas with over 0 total?
- Gold: `{"sel": 3, "conds": [[4, 1, 0], [0, 0, "texas"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "texas"], [4, 1, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:10866:2-11099297-10

- Question: What rank was caerphilly with a Swing smaller than 6.92?
- Gold: `{"sel": 0, "conds": [[3, 2, 6.92], [1, 0, "caerphilly"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "caerphilly"], [3, 2, 6.92]], "sel": 0}`
- Error: logical-form mismatch

## test:10888:2-11171219-1

- Question: What was the attendance on October 27, 1968?
- Gold: `{"sel": 0, "conds": [[1, 0, "october 27, 1968"]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "October 27, 1968"]], "sel": 4}`
- Error: logical-form mismatch

## test:10889:2-11171219-1

- Question: What was the attendance on November 3, 1968, that was a week smaller than 8?
- Gold: `{"sel": 4, "conds": [[1, 0, "november 3, 1968"], [0, 2, 8]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "November 3, 1968"], [0, 2, 8]], "sel": 4}`
- Error: logical-form mismatch

## test:10905:2-11399628-28

- Question: How many appearances for psv eindhoven ranked above 11?
- Gold: `{"sel": 4, "conds": [[2, 0, "psv eindhoven"], [0, 2, 11]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "PSV Eindhoven"], [0, 1, 11]], "sel": 4}`
- Error: logical-form mismatch

## test:10915:2-1139299-1

- Question: How many games were lost by more than 27 but not more 78 with goals less than 300?
- Gold: `{"sel": 1, "conds": [[2, 1, 27], [4, 2, 78], [6, 2, 300]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[2, 1, 27], [4, 2, 78], [6, 2, 300]], "sel": 1}`
- Error: logical-form mismatch

## test:10933:2-10809444-19

- Question: What did the team score when playing against home in geelong?
- Gold: `{"sel": 3, "conds": [[0, 0, "geelong"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "geelong"]], "sel": 1}`
- Error: logical-form mismatch

## test:10943:2-11516217-44

- Question: What is the total number of runs when the average was less than 31.25 and there were fewer than 24 innings?
- Gold: `{"sel": 3, "conds": [[4, 1, 31.25], [1, 2, 24]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[4, 2, 31.25], [1, 2, 24]], "sel": 3}`
- Error: logical-form mismatch

## test:10945:2-11516217-44

- Question: What is the number of Not Outs when there were more than 327 runs and 24 innings, and an average of 29.54
- Gold: `{"sel": 2, "conds": [[3, 1, 327], [1, 1, 24], [4, 0, 29.54]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 1, 327], [1, 0, 24], [4, 0, 29.54]], "sel": 2}`
- Error: logical-form mismatch

## test:10954:2-11946231-2

- Question: Which model's chipset is intel 955?
- Gold: `{"sel": 3, "conds": [[2, 0, "intel 955"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "intel 955"]], "sel": 0}`
- Error: logical-form mismatch

## test:10973:2-10806852-11

- Question: What is the crowd total for glenferrie oval?
- Gold: `{"sel": 5, "conds": [[4, 0, "glenferrie oval"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[4, 0, "glenferrie oval"]], "sel": 5}`
- Error: logical-form mismatch

## test:10987:2-11086216-2

- Question: What film won best actress at the 2007 Inside Soap Awards?
- Gold: `{"sel": 4, "conds": [[2, 0, "inside soap awards"], [3, 0, "best actress"], [0, 0, 2007]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "won"], [3, 0, "best actress"], [0, 0, 2007], [2, 0, "inside soap awards"]], "sel": 4}`
- Error: logical-form mismatch

## test:10988:2-11086216-2

- Question: What character won the best dramatic performance award?
- Gold: `{"sel": 5, "conds": [[3, 0, "best dramatic performance"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "won"], [3, 0, "best dramatic performance"]], "sel": 5}`
- Error: logical-form mismatch

## test:10989:2-11086216-2

- Question: In what category was character Jacqui Mcqueen nominated before 2011?
- Gold: `{"sel": 3, "conds": [[5, 0, "jacqui mcqueen"], [0, 2, 2011]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "Jacqui McQueen"], [1, 0, "Nominated"], [0, 2, 2011]], "sel": 3}`
- Error: logical-form mismatch

## test:10998:2-1140099-1

- Question: I want the circuit for jim clark
- Gold: `{"sel": 1, "conds": [[4, 0, "jim clark"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "jim clark"]], "sel": 1}`
- Error: logical-form mismatch

## test:11029:2-111574-1

- Question: When 1960 is less than 4,228, 1920 is smaller than 106,021,568 and 1980 is larger than 949, what is the 1970 figure?
- Gold: `{"sel": 6, "conds": [[5, 2, "4,228"], [1, 2, "106,021,568"], [7, 1, 949]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[5, 2, "4,228"], [1, 2, "106,021,568"], [7, 1, 949]], "sel": 6}`
- Error: logical-form mismatch

## test:11031:2-111574-1

- Question: What is the figure in 1940 when 1970 is larger than 11,070 and 1950 is smaller than 150,844,547?
- Gold: `{"sel": 3, "conds": [[6, 1, "11,070"], [4, 2, "150,844,547"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[6, 1, 11070], [4, 2, 150844547]], "sel": 3}`
- Error: logical-form mismatch

## test:11032:2-11994830-21

- Question: What is the number of fumbles for the avg larger than 5.4, with yards smaller than 164?
- Gold: `{"sel": 4, "conds": [[3, 1, 5.4], [2, 2, 164]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[3, 1, 5.4], [2, 2, 164]], "sel": 4}`
- Error: logical-form mismatch

## test:11035:2-12040651-1

- Question: How many appearances with fc igea virtus and 1 goal?
- Gold: `{"sel": 4, "conds": [[2, 0, "fc igea virtus"], [5, 0, 1]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "fc igea virtus"], [5, 0, 1]], "sel": 4}`
- Error: logical-form mismatch

## test:11045:2-1123374-2

- Question: What is the number of the grid for Johnny Herbert with more than 52 laps?
- Gold: `{"sel": 4, "conds": [[0, 0, "johnny herbert"], [2, 1, 52]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Johnny Herbert"], [2, 1, 52]], "sel": 4}`
- Error: logical-form mismatch

## test:11065:2-11218948-5

- Question: Which region in Saint-Simon-Les-Mines has a population smaller than 458?
- Gold: `{"sel": 6, "conds": [[2, 0, "saint-simon-les-mines"], [4, 2, 458]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Saint-Simon-Les-Mines"], [4, 2, 458]], "sel": 6}`
- Error: logical-form mismatch

## test:11066:2-11218948-5

- Question: What is total population of Saint-Agapit (code 33045)?
- Gold: `{"sel": 6, "conds": [[2, 0, "saint-agapit"], [0, 2, 33045]], "agg": 4}`
- Prediction: `{"agg": 4, "conds": [[2, 0, "Saint-Agapit"], [0, 0, 33045]], "sel": 4}`
- Error: logical-form mismatch

## test:11085:2-10809368-3

- Question: Which Venue has a crowd larger than 25,000?
- Gold: `{"sel": 2, "conds": [[5, 1, "25,000"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 1, "25,000"]], "sel": 4}`
- Error: logical-form mismatch

## test:11098:2-10791466-4

- Question: What's the total number of picks of a team that had june longalong?
- Gold: `{"sel": 0, "conds": [[1, 0, "june longalong"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "june longalong"]], "sel": 0}`
- Error: logical-form mismatch

## test:11111:2-11954383-1

- Question: How many golden tickets were given out when the auditions were held in San Francisco, California?
- Gold: `{"sel": 6, "conds": [[1, 0, "san francisco, california"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "San Francisco, California"]], "sel": 6}`
- Error: logical-form mismatch

## test:11134:2-1174162-1

- Question: What is the Area with a Median Age of 38 years, a Population of 2,444, and a Date First Settles as a Suburb prior to 1965?
- Gold: `{"sel": 4, "conds": [[2, 0, "38 years"], [1, 0, "2,444"], [6, 2, 1965]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "38 years"], [1, 0, "2,444"], [6, 2, 1965]], "sel": 4}`
- Error: logical-form mismatch

## test:11140:2-120778-2

- Question: What is the percent yes of Nova Scotia, which had more than 2,410,119 vote yes and less than 51.3 vote no?
- Gold: `{"sel": 2, "conds": [[1, 1, "2,410,119"], [0, 0, "nova scotia"], [4, 2, 51.3]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Nova Scotia"], [1, 1, "2,410,119"], [4, 2, 51.3]], "sel": 2}`
- Error: logical-form mismatch

## test:11141:2-120778-2

- Question: What is the percent yes of Alberta, which had a percent no larger than 60.2?
- Gold: `{"sel": 2, "conds": [[0, 0, "alberta"], [4, 1, 60.2]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Alberta"], [4, 1, 60.2]], "sel": 2}`
- Error: logical-form mismatch

## test:11142:2-120778-2

- Question: What is the total number of yes votes in Newfoundland, which had less than 77,881 vote no?
- Gold: `{"sel": 1, "conds": [[0, 0, "newfoundland"], [3, 2, "77,881"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "Newfoundland"], [3, 2, "77,881"]], "sel": 1}`
- Error: logical-form mismatch

## test:11149:2-11484479-1

- Question: What year is the result 6th in munich, west germany?
- Gold: `{"sel": 0, "conds": [[3, 0, "6th"], [2, 0, "munich, west germany"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "6th"], [2, 0, "Munich , West Germany"]], "sel": 0}`
- Error: logical-form mismatch

## test:11150:2-11484479-1

- Question: What year is the event in athens, greece?
- Gold: `{"sel": 0, "conds": [[2, 0, "athens, greece"]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "athens, greece"]], "sel": 0}`
- Error: logical-form mismatch

## test:11151:2-11484479-1

- Question: What year is the venue in budapest, hungary?
- Gold: `{"sel": 0, "conds": [[2, 0, "budapest, hungary"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "budapest, hungary"]], "sel": 0}`
- Error: logical-form mismatch

## test:11155:2-10790099-10

- Question: How many were in the crowd when there was a game at Junction Oval?
- Gold: `{"sel": 5, "conds": [[4, 0, "junction oval"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "Junction Oval"]], "sel": 5}`
- Error: logical-form mismatch

## test:11160:2-11364413-1

- Question: What week was October 29, 2000?
- Gold: `{"sel": 0, "conds": [[1, 0, "october 29, 2000"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "October 29, 2000"]], "sel": 0}`
- Error: logical-form mismatch

## test:11182:2-12045304-2

- Question: What is the total number of interview scores that have an evening gown score of 9.543 and an average that is bigger than 9.521?
- Gold: `{"sel": 1, "conds": [[3, 0, 9.543], [4, 1, 9.521]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[3, 0, 9.543], [4, 1, 9.521]], "sel": 1}`
- Error: logical-form mismatch

## test:11184:2-12087172-2

- Question: What is the total draw count with 52 goals and less than 15 losses?
- Gold: `{"sel": 5, "conds": [[8, 0, 52], [6, 2, 15]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[8, 0, 52], [6, 2, 15]], "sel": 5}`
- Error: logical-form mismatch

## test:11198:2-10788451-10

- Question: What was the attendance when Hawthorn played as the away team?
- Gold: `{"sel": 5, "conds": [[2, 0, "hawthorn"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "hawthorn"]], "sel": 5}`
- Error: logical-form mismatch

## test:11212:2-11241317-1

- Question: How many stories were done in 2008 with a 16 rank?
- Gold: `{"sel": 3, "conds": [[4, 0, 2008], [0, 0, "16"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, 2008], [0, 0, "16"]], "sel": 3}`
- Error: logical-form mismatch

## test:11214:2-11241317-1

- Question: Name the total number of stories that had a 16 rank
- Gold: `{"sel": 3, "conds": [[0, 0, "16"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "16"]], "sel": 3}`
- Error: logical-form mismatch

## test:11220:2-1123462-2

- Question: Who retired at lap 77 and was grid 11?
- Gold: `{"sel": 3, "conds": [[2, 0, "77"], [4, 0, "11"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "77"], [4, 0, "11"]], "sel": 0}`
- Error: logical-form mismatch

## test:11224:2-1157079-1

- Question: which year has the toyota tf102 chassis?
- Gold: `{"sel": 0, "conds": [[2, 0, "toyota tf102"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Toyota TF102"]], "sel": 0}`
- Error: logical-form mismatch

## test:11232:2-10808089-3

- Question: Who was the Away team at Hawthorn?
- Gold: `{"sel": 0, "conds": [[2, 0, "hawthorn"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "hawthorn"]], "sel": 2}`
- Error: logical-form mismatch

## test:11233:2-10808089-3

- Question: Which team has an away score of 7.4 (46)?
- Gold: `{"sel": 1, "conds": [[3, 0, "7.4 (46)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "7.4 (46)"]], "sel": 2}`
- Error: logical-form mismatch

## test:11249:2-10807990-14

- Question: I want to know the crowd with a home team of carlton
- Gold: `{"sel": 5, "conds": [[0, 0, "carlton"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "carlton"]], "sel": 5}`
- Error: logical-form mismatch

## test:11253:2-1110775-1

- Question: what is the population estimate 2005 for the with the area (km2) 3,034.08?
- Gold: `{"sel": 2, "conds": [[1, 0, "3,034.08"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "3,034.08"]], "sel": 2}`
- Error: logical-form mismatch

## test:11299:2-11716268-1

- Question: How many places have more than 33 points?
- Gold: `{"sel": 4, "conds": [[3, 0, 33]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[3, 1, 33]], "sel": 4}`
- Error: logical-form mismatch

## test:11301:2-11716268-1

- Question: What's the highest points for song "budi tu" with draw less than 7?
- Gold: `{"sel": 3, "conds": [[0, 2, 7], [2, 0, "\"budi tu\""]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[2, 0, "budi tu"], [0, 2, 7]], "sel": 3}`
- Error: logical-form mismatch

## test:11317:2-1123244-2

- Question: What is the total number of laps with a Driver of eddie irvine?
- Gold: `{"sel": 2, "conds": [[0, 0, "eddie irvine"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "eddie irvine"]], "sel": 2}`
- Error: logical-form mismatch

## test:11320:2-12070870-1

- Question: What is the sum of wins when the goals for number was bigger than 35, the team was the Montreal Hockey Club, and the number of losses was less than 2?
- Gold: `{"sel": 2, "conds": [[5, 1, 35], [0, 0, "montreal hockey club"], [3, 2, 2]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[5, 1, 35], [0, 0, "Montreal Hockey Club"], [3, 2, 2]], "sel": 2}`
- Error: logical-form mismatch

## test:11322:2-11171707-1

- Question: What was the week of the December 9, 1961 game with an attendance larger than 41,268?
- Gold: `{"sel": 0, "conds": [[1, 0, "december 9, 1961"], [4, 1, "41,268"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "December 9, 1961"], [4, 1, 41268]], "sel": 0}`
- Error: logical-form mismatch

## test:11323:2-11410137-1

- Question: None of the communities listed has a percentage smaller than 8.6 in 2006.
- Gold: `{"sel": 4, "conds": [[1, 2, 8.6]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 2, 8.6]], "sel": 0}`
- Error: logical-form mismatch

## test:11324:2-11410137-1

- Question: There are communities listed that a percentage larger than 7.6 in 2001, but none of them has 2 seats listed in 2006.
- Gold: `{"sel": 4, "conds": [[2, 0, 2], [3, 1, 7.6]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[3, 1, 7.6], [2, 3, 2]], "sel": 0}`
- Error: operator 3 is not executable

## test:11354:2-12072778-5

- Question: What is the top-25 of the U.S. open, which has less than 7 events?
- Gold: `{"sel": 3, "conds": [[0, 0, "u.s. open"], [4, 2, 7]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "U.S. Open"], [4, 2, 7]], "sel": 3}`
- Error: logical-form mismatch

## test:11355:2-12072778-5

- Question: How many events does the tournament with a top-10 of 2 and more than 5 cuts have?
- Gold: `{"sel": 4, "conds": [[2, 0, 2], [5, 1, 5]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, 2], [5, 1, 5]], "sel": 4}`
- Error: logical-form mismatch

## test:11373:2-11622318-3

- Question: How much money did the player ranked above 3 with under 28 events earn?
- Gold: `{"sel": 3, "conds": [[4, 2, 28], [0, 2, 3]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 1, 3], [4, 2, 28]], "sel": 3}`
- Error: logical-form mismatch

## test:11376:2-11055438-10

- Question: What is the exact number of Total that has a percentage of precisely 12.03%?
- Gold: `{"sel": 3, "conds": [[4, 0, "12.03%"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "12.03%"]], "sel": 3}`
- Error: logical-form mismatch

## test:11383:2-11636955-15

- Question: What is the rd number where the reg GP is 0 and the pick is 150?
- Gold: `{"sel": 0, "conds": [[4, 0, 0], [1, 0, 150]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, 0], [1, 0, 150]], "sel": 0}`
- Error: logical-form mismatch

## test:11384:2-1171713-1

- Question: What season had a position higher than 11 and an attendance per game of 9,153?
- Gold: `{"sel": 0, "conds": [[4, 0, "9,153"], [3, 1, 11]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[3, 1, 11], [4, 0, "9,153"]], "sel": 0}`
- Error: logical-form mismatch

## test:11420:2-1122987-1

- Question: How many laps are associated with a time of + 1:39.591?
- Gold: `{"sel": 2, "conds": [[3, 0, "+ 1:39.591"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "+ 1:39.591"]], "sel": 2}`
- Error: logical-form mismatch

## test:11427:2-12063332-2

- Question: What is the sum number of evening gown stats for New Jersey when the interview was less than 9.344?
- Gold: `{"sel": 3, "conds": [[0, 0, "new jersey"], [1, 2, 9.344]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "New Jersey"], [1, 2, 9.344]], "sel": 3}`
- Error: logical-form mismatch

## test:11432:2-1111814-1

- Question: what is the attendance when the location is veterans stadium, the game is more than 3 and the time is 2:21?
- Gold: `{"sel": 5, "conds": [[3, 0, "veterans stadium"], [0, 1, 3], [4, 0, "2:21"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Veterans Stadium"], [0, 1, 3], [4, 0, "2:21"]], "sel": 5}`
- Error: logical-form mismatch

## test:11435:2-1111814-1

- Question: what is the attendance on the date of october 16 and the game is more than 5?
- Gold: `{"sel": 5, "conds": [[1, 0, "october 16"], [0, 1, 5]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "october 16"], [0, 1, 5]], "sel": 5}`
- Error: logical-form mismatch

## test:11444:2-1145645-1

- Question: What is the total work number of Gowrie with a 0-6-4t type after 1908?
- Gold: `{"sel": 4, "conds": [[2, 0, "0-6-4t"], [0, 0, "gowrie"], [3, 1, 1908]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "Gowrie"], [2, 0, "0-6-4t"], [3, 1, 1908]], "sel": 4}`
- Error: logical-form mismatch

## test:11459:2-1092-1

- Question: what is the crude birth rate (per 1000) when the natural change (per 1000) is more than 31.6 and the average population (x1000) is less than 1,802?
- Gold: `{"sel": 4, "conds": [[6, 1, 31.6], [0, 2, "1,802"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[6, 1, 31.6], [0, 2, "1,802"]], "sel": 4}`
- Error: logical-form mismatch

## test:11461:2-1092-1

- Question: what is the crude birth rate (per 1000) when the crude death rate (per 1000) is less than 6.2, the average population (x1000) is larger than 2,770 and the natural change (per 1000) is 17.2?
- Gold: `{"sel": 4, "conds": [[5, 2, 6.2], [0, 1, "2,770"], [6, 0, 17.2]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[5, 2, 6.2], [0, 1, "2,770"], [6, 0, 17.2]], "sel": 4}`
- Error: logical-form mismatch

## test:11472:2-11677312-2

- Question: Tell me the average size for minor third
- Gold: `{"sel": 1, "conds": [[0, 0, "minor third"]], "agg": 5}`
- Prediction: `{"agg": 5, "conds": [[0, 0, "minor third"]], "sel": 2}`
- Error: logical-form mismatch

## test:11477:2-11173827-1

- Question: With 1.97 million HK viewers and a finale more than 33, what was the total number of peaks?
- Gold: `{"sel": 4, "conds": [[7, 0, "1.97 million"], [6, 1, 33]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[7, 0, "1.97 million"], [6, 1, 33]], "sel": 4}`
- Error: logical-form mismatch

## test:11495:2-11056278-1

- Question: Which person drove a Reynard 2ki with a Honda Hrk engine?
- Gold: `{"sel": 5, "conds": [[1, 0, "reynard 2ki"], [2, 0, "honda hrk"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Reynard 2KI"], [2, 0, "Honda HRK"]], "sel": 4}`
- Error: logical-form mismatch

## test:11513:2-1187808-1

- Question: What is the total track that is translated in brussels?
- Gold: `{"sel": 0, "conds": [[2, 0, "brussels"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[2, 0, "brussels"]], "sel": 0}`
- Error: logical-form mismatch

## test:11530:2-1108394-43

- Question: How many voters were in Manhattan when 181,639 people voted in the Bronx?
- Gold: `{"sel": 5, "conds": [[2, 0, "181,639"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "181,639"]], "sel": 1}`
- Error: logical-form mismatch

## test:11535:2-11622496-3

- Question: What is the total number of events that Al Geiberger has played with earnings larger than 527,033?
- Gold: `{"sel": 4, "conds": [[1, 0, "al geiberger"], [3, 1, "527,033"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "Al Geiberger"], [3, 1, "527,033"]], "sel": 4}`
- Error: logical-form mismatch

## test:11538:2-12003874-2

- Question: What is the highest round in the Wec 25 match in Las Vegas, Nevada, United States?
- Gold: `{"sel": 5, "conds": [[6, 0, "las vegas, nevada, united states"], [4, 0, "wec 25"]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[4, 0, "WEC 25"], [6, 0, "Las Vegas, Nevada , United States"]], "sel": 5}`
- Error: logical-form mismatch

## test:11546:2-10806592-2

- Question: In the game where the crowd was 11,327 and the hoem team scored 13.17 (95) How much did the away team score?
- Gold: `{"sel": 2, "conds": [[5, 1, "11,327"], [1, 0, "13.17 (95)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "11,327"], [1, 0, "13.17 (95)"]], "sel": 3}`
- Error: logical-form mismatch

## test:11552:2-1083851-2

- Question: How many people attended games at alberto picco stadium?
- Gold: `{"sel": 3, "conds": [[2, 0, "alberto picco"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "alberto picco"]], "sel": 3}`
- Error: logical-form mismatch

## test:11555:2-11821711-7

- Question: What is the total attendance of the game with Toronto as the visitor team?
- Gold: `{"sel": 5, "conds": [[1, 0, "toronto"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "toronto"]], "sel": 5}`
- Error: logical-form mismatch

## test:11558:2-10981660-1

- Question: How many tons was the ship from norway?
- Gold: `{"sel": 2, "conds": [[3, 0, "norway"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "norway"]], "sel": 2}`
- Error: logical-form mismatch

## test:11560:2-10790651-4

- Question: How many people were in attendance at Glenferrie Oval?
- Gold: `{"sel": 5, "conds": [[4, 0, "glenferrie oval"]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "Glenferrie Oval"]], "sel": 5}`
- Error: logical-form mismatch

## test:11567:2-12079804-1

- Question: What is the total for the state of new york and a swimsuit less than 9.394?
- Gold: `{"sel": 1, "conds": [[0, 0, "new york"], [2, 2, 9.394]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "New York"], [2, 2, 9.394]], "sel": 0}`
- Error: logical-form mismatch

## test:11571:2-11233358-6

- Question: What day was the score 3-0 after 2011?
- Gold: `{"sel": 1, "conds": [[3, 0, "3-0"], [0, 0, 2011]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "3-0"], [0, 1, 2011]], "sel": 1}`
- Error: logical-form mismatch

## test:11576:2-1157732-1

- Question: How many bronzes for the nation with 2 golds and ranked below 2?
- Gold: `{"sel": 4, "conds": [[2, 0, 2], [0, 1, 2]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, 2], [0, 1, 2]], "sel": 4}`
- Error: logical-form mismatch

## test:11588:2-10808681-6

- Question: What was the attendance of the South Melbourne away game?
- Gold: `{"sel": 5, "conds": [[2, 0, "south melbourne"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "South Melbourne"]], "sel": 5}`
- Error: logical-form mismatch

## test:11595:2-11268916-3

- Question: When the shares were less than 8, how many total viewers were there?
- Gold: `{"sel": 4, "conds": [[2, 2, 8]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[2, 2, 8]], "sel": 4}`
- Error: logical-form mismatch

## test:11605:2-11513685-5

- Question: Who lost on July 20 with 42,607 attending?
- Gold: `{"sel": 3, "conds": [[4, 1, "42,607"], [0, 0, "july 20"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "July 20"], [4, 0, 42607]], "sel": 3}`
- Error: logical-form mismatch

## test:11615:2-1125581-1

- Question: What is the election year of the president with a Birth State of lost connecticut?
- Gold: `{"sel": 1, "conds": [[3, 0, "lost connecticut"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "lost connecticut"]], "sel": 1}`
- Error: logical-form mismatch

## test:11629:2-10887379-5

- Question: How many people attended games at vfl park?
- Gold: `{"sel": 5, "conds": [[4, 0, "vfl park"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "vfl park"]], "sel": 5}`
- Error: logical-form mismatch

## test:11636:2-10790397-1

- Question: How many were in the crowd when North Melbourne was the home team?
- Gold: `{"sel": 5, "conds": [[0, 0, "north melbourne"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "north melbourne"]], "sel": 5}`
- Error: logical-form mismatch

## test:11648:2-12050358-2

- Question: What is the number for evening gown in kansas with less than 9.357 interviews?
- Gold: `{"sel": 3, "conds": [[0, 0, "kansas"], [1, 2, 9.357]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Kansas"], [1, 2, 9.357]], "sel": 3}`
- Error: logical-form mismatch

## test:11676:2-12010417-1

- Question: What is the sum number of bronzes when the rank is less than 2 and the gold is less than 1?
- Gold: `{"sel": 4, "conds": [[0, 2, 2], [2, 2, 1]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 2, 2], [2, 2, 1]], "sel": 4}`
- Error: logical-form mismatch

## test:11678:2-12015401-2

- Question: What is the Average for South Carolina with an Interview less than 9.626?
- Gold: `{"sel": 4, "conds": [[0, 0, "south carolina"], [1, 2, 9.626]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "South Carolina"], [1, 2, 9.626]], "sel": 4}`
- Error: logical-form mismatch

## test:11691:2-11677694-13

- Question: How many games have an Order of 1006, and Goals larger than 192?
- Gold: `{"sel": 3, "conds": [[0, 0, 1006], [4, 1, 192]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, 1006], [4, 1, 192]], "sel": 3}`
- Error: logical-form mismatch

## test:11693:2-11409339-1

- Question: What is the latest year in Annecy, France?
- Gold: `{"sel": 0, "conds": [[2, 0, "annecy, france"]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[2, 0, "Annecy , France"]], "sel": 0}`
- Error: logical-form mismatch

## test:11695:2-11870934-6

- Question: How many people attended the game on january 10 with a Score of 3 – 2?
- Gold: `{"sel": 5, "conds": [[2, 0, "3 – 2"], [0, 0, "january 10"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "january 10"], [2, 0, "3 – 2"]], "sel": 5}`
- Error: logical-form mismatch

## test:11699:2-12020197-2

- Question: How many laps by Jorge Lorenzo on the Aprilia with a grid bigger than 1?
- Gold: `{"sel": 2, "conds": [[1, 0, "aprilia"], [0, 0, "jorge lorenzo"], [4, 1, 1]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Jorge Lorenzo"], [1, 0, "Aprilia"], [4, 1, 1]], "sel": 2}`
- Error: logical-form mismatch

## test:11706:2-1122547-1

- Question: How many laps have a Time/Retired of + 4 laps, and a Driver of graham hill?
- Gold: `{"sel": 2, "conds": [[3, 0, "+ 4 laps"], [0, 0, "graham hill"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "+ 4 laps"], [0, 0, "graham hill"]], "sel": 2}`
- Error: logical-form mismatch

## test:11759:2-11827596-1

- Question: Which year was the film Rang Barse introduced?
- Gold: `{"sel": 0, "conds": [[1, 0, "rang barse"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Rang Barse"]], "sel": 0}`
- Error: logical-form mismatch

## test:11779:2-11163017-5

- Question: What is Ivaiporã, pr's biggest population?
- Gold: `{"sel": 1, "conds": [[0, 0, "ivaiporã, pr"]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[0, 0, "Ivaiporã , PR"]], "sel": 1}`
- Error: logical-form mismatch

## test:11803:2-11840017-1

- Question: What is the number of Goals For for Games Played more than 8?
- Gold: `{"sel": 5, "conds": [[1, 1, 8]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[1, 1, 8]], "sel": 5}`
- Error: logical-form mismatch

## test:11810:2-1080291-2

- Question: Which vehicle has a Diagram of 516 or smaller, and a driving motor brake second (dmbs) type.
- Gold: `{"sel": 2, "conds": [[3, 1, 516], [1, 0, "driving motor brake second (dmbs)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 2, 516], [1, 0, "driving motor brake second (dmbs)"]], "sel": 0}`
- Error: logical-form mismatch

## test:11823:2-10808346-11

- Question: What is the away team that plays at Punt Road Oval?
- Gold: `{"sel": 3, "conds": [[4, 0, "punt road oval"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "punt road oval"]], "sel": 2}`
- Error: logical-form mismatch

## test:11836:2-11786815-10

- Question: What is the total attendance for Detroit on hasek?
- Gold: `{"sel": 5, "conds": [[3, 0, "detroit"], [4, 0, "hasek"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[3, 0, "Detroit"], [4, 0, "Hasek"]], "sel": 5}`
- Error: logical-form mismatch

## test:11845:2-11093080-8

- Question: Which team has a Losses value larger than 1 and a Wins value smaller than 0?
- Gold: `{"sel": 5, "conds": [[3, 1, 1], [1, 2, 0]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[3, 1, 1], [1, 2, 0]], "sel": 0}`
- Error: logical-form mismatch

## test:11846:2-11206685-2

- Question: In guangzhou, who won the game with a score of 1-0?
- Gold: `{"sel": 5, "conds": [[1, 0, "guangzhou"], [4, 0, "1-0"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Guangzhou"], [4, 0, "1-0"]], "sel": 3}`
- Error: logical-form mismatch

## test:11852:2-11783707-4

- Question: What is the average for the RB with an 8 yard long?
- Gold: `{"sel": 3, "conds": [[5, 0, 8]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, 8]], "sel": 3}`
- Error: logical-form mismatch

## test:11853:2-11783707-4

- Question: How many yards for the RB with over 4 carries, 2 TDs, and a long greater than 8?
- Gold: `{"sel": 2, "conds": [[1, 1, 4], [4, 0, 2], [5, 1, 8]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 1, 4], [4, 0, 2], [5, 1, 8]], "sel": 2}`
- Error: logical-form mismatch

## test:11855:2-12094300-1

- Question: What is the preliminaries of the contestant from Massachusetts with an evening gown higher than 8.631, an average less than 8.791, and an interview higher than 8.608?
- Gold: `{"sel": 1, "conds": [[4, 1, 8.631], [5, 2, 8.791], [0, 0, "massachusetts"], [2, 1, 8.608]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Massachusetts"], [4, 1, 8.631], [5, 2, 8.791], [2, 1, 8.608]], "sel": 1}`
- Error: logical-form mismatch

## test:11858:2-12094300-1

- Question: What is the evening gown score of the contestant from the District of Columbia with preliminaries smaller than 8.647?
- Gold: `{"sel": 4, "conds": [[1, 2, 8.647], [0, 0, "district of columbia"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "District of Columbia"], [1, 2, 8.647]], "sel": 4}`
- Error: logical-form mismatch

## test:11864:2-11308227-4

- Question: Whose reign ended in Egypt?
- Gold: `{"sel": 3, "conds": [[1, 0, "egypt"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Egypt"]], "sel": 0}`
- Error: logical-form mismatch

## test:11865:2-11308227-4

- Question: Whose reign ended in Afghanistan after 3 days?
- Gold: `{"sel": 3, "conds": [[4, 0, "3 days"], [1, 0, "afghanistan"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Afghanistan"], [4, 0, "3 days"]], "sel": 0}`
- Error: logical-form mismatch

## test:11866:2-11308227-4

- Question: Whose reign began in Vietnam and ended in October 1005?
- Gold: `{"sel": 2, "conds": [[1, 0, "vietnam"], [3, 0, "october 1005"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Vietnam"], [3, 0, "October 1005"]], "sel": 0}`
- Error: logical-form mismatch

## test:11874:2-11021760-1

- Question: what is the number of points when the place is less than 7, the draw is more than 2 and the artist is piece of cake?
- Gold: `{"sel": 3, "conds": [[4, 2, 7], [0, 1, 2], [1, 0, "piece of cake"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 2, 7], [0, 1, 2], [1, 0, "piece of cake"]], "sel": 3}`
- Error: logical-form mismatch

## test:11887:2-1122970-1

- Question: How many laps for grid 12?
- Gold: `{"sel": 2, "conds": [[4, 0, 12]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 0, 12]], "sel": 2}`
- Error: logical-form mismatch

## test:11888:2-1122970-1

- Question: Who built the 21 grid car that retired due to suspension?
- Gold: `{"sel": 1, "conds": [[4, 1, 21], [3, 0, "suspension"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, 21], [3, 0, "suspension"]], "sel": 1}`
- Error: logical-form mismatch

## test:11891:2-10807673-10

- Question: Which team has an away team score of 9.11 (65)?
- Gold: `{"sel": 0, "conds": [[3, 0, "9.11 (65)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "9.11 (65)"]], "sel": 2}`
- Error: logical-form mismatch

## test:11920:2-10809444-1

- Question: Which team had an away score of 15.14 (104)?
- Gold: `{"sel": 0, "conds": [[3, 0, "15.14 (104)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "15.14 (104)"]], "sel": 2}`
- Error: logical-form mismatch

## test:11926:2-11786160-4

- Question: What is the average of the player with 124 yards and less than 13 rec.?
- Gold: `{"sel": 3, "conds": [[2, 0, 124], [1, 2, 13]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 0, 124], [1, 2, 13]], "sel": 3}`
- Error: logical-form mismatch

## test:11962:2-10818970-6

- Question: What was the score of cook 3/6?
- Gold: `{"sel": 3, "conds": [[5, 0, "cook 3/6"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "Cook 3/6"]], "sel": 4}`
- Error: logical-form mismatch

## test:11969:2-11512596-5

- Question: How many people attended on July 5?
- Gold: `{"sel": 4, "conds": [[0, 0, "july 5"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "July 5"]], "sel": 4}`
- Error: logical-form mismatch

## test:11970:2-1195142-4

- Question: Which production won the drama desk award as well as the category of outstanding sound design?
- Gold: `{"sel": 4, "conds": [[1, 0, "drama desk award"], [2, 0, "outstanding sound design"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Drama Desk Award"], [2, 0, "Outstanding Sound Design"], [4, 0, "Won"]], "sel": 3}`
- Error: logical-form mismatch

## test:11972:2-1195142-4

- Question: In what year was Terry Johnson nominated for a Tony award?
- Gold: `{"sel": 0, "conds": [[1, 0, "tony award"], [3, 0, "terry johnson"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "terry johnson"], [1, 0, "tony award"]], "sel": 0}`
- Error: logical-form mismatch

## test:11977:2-10869537-17

- Question: What was the attendance when St Kilda played as the away team?
- Gold: `{"sel": 5, "conds": [[2, 0, "st kilda"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "St Kilda"]], "sel": 5}`
- Error: logical-form mismatch

## test:11999:2-11096996-1

- Question: Which Superfund site has the CERCLIS ID fld980494959?
- Gold: `{"sel": 3, "conds": [[0, 0, "fld980494959"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "fld980494959"]], "sel": 1}`
- Error: logical-form mismatch

## test:12065:2-11677760-15

- Question: What college picked someone from The Episcopal Academy?
- Gold: `{"sel": 4, "conds": [[2, 0, "episcopal academy"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "The Episcopal Academy"]], "sel": 4}`
- Error: logical-form mismatch

## test:12072:2-11827596-4

- Question: What 1972 Hindi film had Ravindra Jain directing the music?
- Gold: `{"sel": 1, "conds": [[0, 1, 1972], [4, 0, "hindi"], [3, 0, "ravindra jain"], [2, 0, "ravindra jain"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 1972], [2, 0, "Ravindra Jain"], [4, 0, "Hindi"]], "sel": 1}`
- Error: logical-form mismatch

## test:12074:2-11384351-1

- Question: Which driver has a # smaller than 40, less than 151 points, and Winnings of $84,400?
- Gold: `{"sel": 2, "conds": [[1, 2, 40], [3, 2, 151], [5, 0, "$84,400"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 2, 40], [3, 2, 151], [5, 0, "$84,400"]], "sel": 0}`
- Error: logical-form mismatch

## test:12075:2-11384351-1

- Question: Which driver has less than 61 points, but winnings of $67,675?
- Gold: `{"sel": 4, "conds": [[5, 0, "$67,675"], [3, 2, 61]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[3, 2, 61], [5, 0, "$67,675"]], "sel": 0}`
- Error: logical-form mismatch

## test:12076:2-11384351-1

- Question: Which driver has the highest point total after winning $133,386?
- Gold: `{"sel": 3, "conds": [[5, 0, "$133,386"]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "$133,386"]], "sel": 0}`
- Error: logical-form mismatch

## test:12078:2-11327266-9

- Question: When the points are less than 65 what is the drop #?
- Gold: `{"sel": 5, "conds": [[0, 2, 65]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 2, 65]], "sel": 5}`
- Error: logical-form mismatch

## test:12086:2-10869537-11

- Question: What was the crowd size when st kilda played home?
- Gold: `{"sel": 5, "conds": [[0, 0, "st kilda"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "st kilda"]], "sel": 5}`
- Error: logical-form mismatch

## test:12110:2-11467154-1

- Question: How many points does Draw 5 have?
- Gold: `{"sel": 3, "conds": [[0, 0, 5]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 0, 5]], "sel": 3}`
- Error: logical-form mismatch

## test:12112:2-11467154-1

- Question: The song "Before the Clock Strikes 12" has 55 points. What number did the song place?
- Gold: `{"sel": 4, "conds": [[2, 0, "\"before the clock strikes 12\""], [3, 1, 55]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Before The Clock Strikes 12"], [3, 0, 55]], "sel": 4}`
- Error: logical-form mismatch

## test:12145:2-17732555-7

- Question: WHAT ARE THE BYES WITH A WIN SMALLER THAN 16, 8 LOSSES, AND AT PENSHURST, WITH AGAINST SMALLER THAN 1405?
- Gold: `{"sel": 2, "conds": [[1, 2, 16], [3, 0, 8], [0, 0, "penshurst"], [5, 2, 1405]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 2, 16], [3, 0, 8], [0, 0, "Penshurst"], [5, 2, 1405]], "sel": 2}`
- Error: logical-form mismatch

## test:12146:2-17732555-7

- Question: WHAT ARE THE BYES WITH A DRAWS OF 1, SMW ROVERS, AND WINS LARGER THAN 6?
- Gold: `{"sel": 2, "conds": [[4, 0, 1], [0, 0, "smw rovers"], [1, 1, 6]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 0, 1], [0, 0, "SMW Rovers"], [1, 1, 6]], "sel": 2}`
- Error: logical-form mismatch

## test:12152:2-18228282-6

- Question: What is the height of Patrick Femerling, of the Alba Berlin club?
- Gold: `{"sel": 1, "conds": [[4, 0, "alba berlin"], [0, 0, "patrick femerling"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Patrick Femerling"], [4, 0, "ALBA Berlin"]], "sel": 1}`
- Error: logical-form mismatch

## test:12168:2-18212767-1

- Question: How many tries for were there 48 points?
- Gold: `{"sel": 6, "conds": [[10, 0, "48"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[10, 0, "48"]], "sel": 6}`
- Error: logical-form mismatch

## test:12178:2-1787654-3

- Question: What is the total number of seats with gavin duffy in series 4?
- Gold: `{"sel": 0, "conds": [[3, 0, "gavin duffy"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[3, 0, "gavin duffy"]], "sel": 0}`
- Error: logical-form mismatch

## test:12181:2-17837478-2

- Question: What is the lowest position of the club with 53 goals against, 26 points, and a -11 goal difference?
- Gold: `{"sel": 0, "conds": [[8, 0, 53], [3, 0, 26], [9, 1, -11]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[8, 0, 53], [3, 0, 26], [9, 0, -11]], "sel": 0}`
- Error: logical-form mismatch

## test:12188:2-17798269-3

- Question: What was the score for the game played on October 16, with an attendance of 14,945 and a decision of Raycroft?
- Gold: `{"sel": 2, "conds": [[4, 1, "14,945"], [3, 0, "raycroft"], [0, 0, "october 16"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "october 16"], [4, 0, "14,945"], [3, 0, "raycroft"]], "sel": 2}`
- Error: logical-form mismatch

## test:12190:2-1833981-4

- Question: What Result has a Location of atlanta, and Rank smaller than 4?
- Gold: `{"sel": 1, "conds": [[4, 0, "atlanta"], [0, 2, 4]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "atlanta"], [0, 2, 4]], "sel": 1}`
- Error: logical-form mismatch

## test:12202:2-18018248-4

- Question: How many goals scored have utenis utena as the club, with wins less than 8?
- Gold: `{"sel": 6, "conds": [[1, 0, "utenis utena"], [3, 2, 8]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "Utenis Utena"], [3, 2, 8]], "sel": 6}`
- Error: logical-form mismatch

## test:12203:2-18018248-4

- Question: How many points have utenis utena as the club, with loses less than 16?
- Gold: `{"sel": 8, "conds": [[1, 0, "utenis utena"], [5, 1, 16]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "Utenis Utena"], [5, 2, 16]], "sel": 8}`
- Error: logical-form mismatch

## test:12204:2-18018248-4

- Question: How many loses have points greater than 30, goals scored greater than 59, with a position greater than 5?
- Gold: `{"sel": 5, "conds": [[8, 1, 30], [6, 1, 59], [0, 1, 5]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[8, 1, 30], [6, 1, 59], [0, 1, 5]], "sel": 5}`
- Error: logical-form mismatch

## test:12225:2-18164207-2

- Question: What is the total to par with a total of 163?
- Gold: `{"sel": 4, "conds": [[3, 0, 163]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[3, 0, 163]], "sel": 4}`
- Error: logical-form mismatch

## test:12226:2-18164207-2

- Question: What is the total for a to par bigger than 7 and a player of al geiberger?
- Gold: `{"sel": 3, "conds": [[0, 0, "al geiberger"], [4, 1, 7]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[4, 1, 7], [0, 0, "al geiberger"]], "sel": 3}`
- Error: logical-form mismatch

## test:12227:2-1792861-21

- Question: What is the 1 vs 2 when 2 vs 3 is less than 15 and total is less than 30?
- Gold: `{"sel": 1, "conds": [[3, 2, 15], [4, 2, 30]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 2, 15], [4, 2, 30]], "sel": 1}`
- Error: logical-form mismatch

## test:12229:2-1792861-21

- Question: What is the total when 2 vs 3 is less than 15 and 1 vs 3 is 7?
- Gold: `{"sel": 4, "conds": [[3, 2, 15], [2, 0, 7]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 2, 15], [2, 0, 7]], "sel": 4}`
- Error: logical-form mismatch

## test:12230:2-1792861-21

- Question: What is the 2 vs 3 when total is bigger than 38?
- Gold: `{"sel": 3, "conds": [[4, 1, 38]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 1, 38]], "sel": 3}`
- Error: logical-form mismatch

## test:12231:2-1792861-21

- Question: What is the total when preferences is c > b > a and 1 vs 2 is less than 15?
- Gold: `{"sel": 4, "conds": [[0, 0, "c > b > a"], [1, 2, 15]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "c > b > a"], [1, 2, 15]], "sel": 4}`
- Error: logical-form mismatch

## test:12243:2-18064020-18

- Question: What's the total long for an avg/g over 0.2, fewer than 2 loss, and a gain less than 8?
- Gold: `{"sel": 4, "conds": [[5, 1, 0.2], [3, 2, 2], [2, 2, 8]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[5, 1, 0.2], [3, 2, 2], [2, 2, 8]], "sel": 4}`
- Error: logical-form mismatch

## test:12244:2-18064020-18

- Question: What's cameron dantley's total avg/g for loss less than 35?
- Gold: `{"sel": 5, "conds": [[0, 0, "cameron dantley"], [3, 2, 35]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "cameron dantley"], [3, 2, 35]], "sel": 5}`
- Error: logical-form mismatch

## test:12257:2-17841376-1

- Question: How much Jury has an Artist of chalice & maagiline kuues, and a Draw smaller than 5?
- Gold: `{"sel": 3, "conds": [[1, 0, "chalice & maagiline kuues"], [0, 2, 5]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "chalice & maagiline kuues"], [0, 2, 5]], "sel": 3}`
- Error: logical-form mismatch

## test:12266:2-17660359-6

- Question: WHAT IS THE TOTAL WITH A NANQUAN OF 9.72, RANK BIGGER THAN 3, NANGUN SMALLER THAN 9.5?
- Gold: `{"sel": 4, "conds": [[2, 0, 9.72], [0, 1, 3], [3, 2, 9.5]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[2, 0, 9.72], [0, 1, 3], [3, 2, 9.5]], "sel": 4}`
- Error: logical-form mismatch

## test:12271:2-1777876-1

- Question: How many households have a Median household income of $43,889?
- Gold: `{"sel": 5, "conds": [[2, 0, "$43,889"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "$43,889"]], "sel": 5}`
- Error: logical-form mismatch

## test:12283:2-18261246-3

- Question: Which Round has an Event of 200 miles of norisring?
- Gold: `{"sel": 0, "conds": [[2, 0, "200 miles of norisring"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "200 miles of norisring"]], "sel": 0}`
- Error: logical-form mismatch

## test:12290:2-18334920-1

- Question: What is the total of built with a flag of panama?
- Gold: `{"sel": 0, "conds": [[4, 0, "panama"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[4, 0, "panama"]], "sel": 0}`
- Error: logical-form mismatch

## test:12329:2-17922286-1

- Question: Which Number of electorates (2009) has a District of jhajjar, and a Reserved for (SC/ST/None) of sc, and a Constituency number smaller than 66?
- Gold: `{"sel": 4, "conds": [[3, 0, "jhajjar"], [2, 0, "sc"], [0, 2, 66]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "jhajjar"], [2, 0, "sc"], [0, 2, 66]], "sel": 4}`
- Error: logical-form mismatch

## test:12332:2-1794747-6

- Question: What are the years that had someone nominated for best supporting actress?
- Gold: `{"sel": 0, "conds": [[4, 0, "nominated"], [2, 0, "best supporting actress"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "best supporting actress"]], "sel": 0}`
- Error: logical-form mismatch

## test:12378:2-17824926-16

- Question: What was the position of the player picked at 243?
- Gold: `{"sel": 3, "conds": [[2, 1, 243]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, 243]], "sel": 3}`
- Error: logical-form mismatch

## test:12388:2-1825661-1

- Question: What's the total number built with a chassis code of w108.057?
- Gold: `{"sel": 3, "conds": [[1, 0, "w108.057"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "w108.057"]], "sel": 3}`
- Error: logical-form mismatch

## test:12401:2-17837782-2

- Question: Which Draws have a Club of burgos cf, and a Position larger than 8?
- Gold: `{"sel": 5, "conds": [[1, 0, "burgos cf"], [0, 1, 8]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "burgos cf"], [0, 1, 8]], "sel": 5}`
- Error: logical-form mismatch

## test:12402:2-17837782-2

- Question: Which Played has a Goal Difference larger than 24?
- Gold: `{"sel": 2, "conds": [[9, 1, 24]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[9, 1, 24]], "sel": 2}`
- Error: logical-form mismatch

## test:12403:2-17837782-2

- Question: Which Goals against has Wins of 13, and Goals for larger than 42, and more than 9 Losses?
- Gold: `{"sel": 8, "conds": [[4, 0, 13], [7, 1, 42], [6, 1, 9]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 0, 13], [7, 1, 42], [6, 1, 9]], "sel": 8}`
- Error: logical-form mismatch

## test:12404:2-17837782-2

- Question: How many draws have less than 8 wins, and 31 goals for?
- Gold: `{"sel": 5, "conds": [[4, 2, 8], [7, 0, 31]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[4, 2, 8], [7, 0, 31]], "sel": 5}`
- Error: logical-form mismatch

## test:12430:2-17873606-3

- Question: Which Run 4 has a Country of united states, and an Athlete of bree schaaf emily azevedo, and a Run 3 smaller than 58.04?
- Gold: `{"sel": 5, "conds": [[1, 0, "united states"], [0, 0, "bree schaaf emily azevedo"], [4, 2, 58.04]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "united states"], [0, 0, "bree schaaf emily azevedo"], [4, 2, 58.04]], "sel": 5}`
- Error: logical-form mismatch

## test:12431:2-17873606-3

- Question: How much Run 2 has a Run 4 of 57.68, and a Run 3 smaller than 57.9?
- Gold: `{"sel": 3, "conds": [[5, 0, 57.68], [4, 2, 57.9]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, 57.68], [4, 2, 57.9]], "sel": 3}`
- Error: logical-form mismatch

## test:12432:2-17873606-3

- Question: Which Run 4 has a Run 1 of 57.37, and a Run 3 smaller than 57.45?
- Gold: `{"sel": 5, "conds": [[2, 0, 57.37], [4, 2, 57.45]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, 57.37], [4, 2, 57.45]], "sel": 5}`
- Error: logical-form mismatch

## test:12451:2-18127126-3

- Question: How many gold medals for the nation ranked 6?
- Gold: `{"sel": 2, "conds": [[0, 0, "6"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 0, 6]], "sel": 2}`
- Error: logical-form mismatch

## test:12455:2-18111054-1

- Question: Count the Number of electorates (2009) that has a District of fatehpur and  jahanabad?
- Gold: `{"sel": 4, "conds": [[3, 0, "fatehpur"], [1, 0, "jahanabad"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "fatehpur"], [1, 0, "jahanabad"]], "sel": 4}`
- Error: logical-form mismatch

## test:12475:2-17732555-5

- Question: What is the sum of losses when draws are larger than 0?
- Gold: `{"sel": 3, "conds": [[4, 1, 0]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[4, 1, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:12477:2-17732555-5

- Question: What is the sum of byes when wins are 8, and losses are larger than 10?
- Gold: `{"sel": 2, "conds": [[1, 0, 8], [3, 1, 10]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, 8], [3, 1, 10]], "sel": 2}`
- Error: logical-form mismatch

## test:12523:2-17982205-2

- Question: Which Byes have an Against larger than 1235, and Losses smaller than 10, and Wins larger than 7?
- Gold: `{"sel": 2, "conds": [[5, 1, 1235], [3, 2, 10], [1, 1, 7]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[5, 1, 1235], [3, 2, 10], [1, 1, 7]], "sel": 2}`
- Error: logical-form mismatch

## test:12525:2-17982205-2

- Question: Which Draws have a Lexton Plains of skipton, and an Against larger than 1212?
- Gold: `{"sel": 4, "conds": [[0, 0, "skipton"], [5, 1, 1212]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "skipton"], [5, 1, 1212]], "sel": 4}`
- Error: logical-form mismatch

## test:12540:2-17982145-1

- Question: When Benalla DFL is swanpool with less than 16 losses, what is the sum of Byes?
- Gold: `{"sel": 4, "conds": [[0, 0, "swanpool"], [2, 2, 16]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "swanpool"], [2, 2, 16]], "sel": 4}`
- Error: logical-form mismatch

## test:12585:2-17858093-1

- Question: What is the capacity of Bandırma Banvit?
- Gold: `{"sel": 3, "conds": [[0, 0, "bandırma banvit"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Bandırma Banvit"]], "sel": 3}`
- Error: logical-form mismatch

## test:12587:2-18354377-1

- Question: What was the latest year with a position of 1st at Maputo, Mozambique?
- Gold: `{"sel": 0, "conds": [[3, 0, "1st"], [2, 0, "maputo, mozambique"]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[2, 0, "Maputo , Mozambique"], [3, 0, "1st"]], "sel": 0}`
- Error: logical-form mismatch

## test:12594:2-18054397-11

- Question: What is the total attendance when Stourbridge is the home team?
- Gold: `{"sel": 4, "conds": [[1, 0, "stourbridge"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "Stourbridge"]], "sel": 4}`
- Error: logical-form mismatch

## test:12603:2-17982176-2

- Question: What is the total number of wins of the central murray of koondrook-barham, which has more than 0 draws?
- Gold: `{"sel": 1, "conds": [[0, 0, "koondrook-barham"], [4, 1, 0]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "koondrook-barham"], [4, 1, 0]], "sel": 1}`
- Error: logical-form mismatch

## test:12611:2-1824778-1

- Question: What is the total Launches to date with a Version of 541, and CCBs smaller than 1?
- Gold: `{"sel": 7, "conds": [[0, 0, "541"], [2, 2, 1]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "541"], [2, 2, 1]], "sel": 7}`
- Error: logical-form mismatch

## test:12624:2-18226024-2

- Question: What is the number in attendance at Los Angeles Memorial Coliseum?
- Gold: `{"sel": 6, "conds": [[5, 0, "los angeles memorial coliseum"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "Los Angeles Memorial Coliseum"]], "sel": 6}`
- Error: logical-form mismatch

## test:12630:2-1777824-1

- Question: What is the population with 41,511 households?
- Gold: `{"sel": 4, "conds": [[5, 0, "41,511"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "41,511"]], "sel": 4}`
- Error: logical-form mismatch

## test:12639:2-17906488-1

- Question: What is the number of electorates (2009) for Hingna?
- Gold: `{"sel": 4, "conds": [[1, 0, "hingna"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Hingna"]], "sel": 4}`
- Error: logical-form mismatch

## test:12643:2-18135572-2

- Question: What is the all games % of All Neutral of 6–3, and a B10 Home of 3–6?
- Gold: `{"sel": 6, "conds": [[9, 0, "6–3"], [3, 0, "3–6"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[9, 0, "6–3"], [3, 0, "3–6"]], "sel": 6}`
- Error: logical-form mismatch

## test:12664:2-18036506-11

- Question: What was the lowest against when the draw was at least 0?
- Gold: `{"sel": 5, "conds": [[4, 1, 0]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[4, 3, 0]], "sel": 5}`
- Error: operator 3 is not executable

## test:12703:2-17732555-9

- Question: How many wins for the team with fewer than 2 byes?
- Gold: `{"sel": 1, "conds": [[2, 2, 2]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[2, 2, 2]], "sel": 1}`
- Error: logical-form mismatch

## test:12704:2-17732555-9

- Question: How many against for the Moyston-Willaura team with 4 losses and fewer than 2 byes?
- Gold: `{"sel": 5, "conds": [[3, 0, 4], [0, 0, "moyston-willaura"], [2, 2, 2]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Moyston-Willaura"], [3, 0, 4], [2, 2, 2]], "sel": 5}`
- Error: logical-form mismatch

## test:12715:2-18156317-1

- Question: When there are more than 126 errors, more than 1253 total attempts, and more than 64 block assists, what is the smallest digs?
- Gold: `{"sel": 9, "conds": [[4, 1, 126], [5, 0, 1253], [11, 1, 64]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[4, 1, 126], [5, 1, 1253], [11, 1, 64]], "sel": 9}`
- Error: logical-form mismatch

## test:12769:2-17968233-1

- Question: What was the 2nd leg that had a first leg of 1-1?
- Gold: `{"sel": 1, "conds": [[2, 0, "1-1"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "1-1"]], "sel": 3}`
- Error: logical-form mismatch

## test:12793:2-17957305-2

- Question: Which Championship has a League Cup larger than 0, and a FA Cup larger than 0?
- Gold: `{"sel": 1, "conds": [[2, 1, 0], [3, 1, 0]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[2, 1, 0], [3, 1, 0]], "sel": 1}`
- Error: logical-form mismatch

## test:12794:2-17957305-2

- Question: Which Championship has a League Cup smaller than 0?
- Gold: `{"sel": 1, "conds": [[2, 2, 0]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 2, 0]], "sel": 1}`
- Error: logical-form mismatch

## test:12801:2-17716320-4

- Question: Which Goal Difference has 28 Points, and a Club of cd cartagena, more than 15 losses?
- Gold: `{"sel": 9, "conds": [[3, 0, 28], [1, 0, "cd cartagena"], [6, 1, 15]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[3, 0, 28], [1, 0, "cd cartagena"], [6, 1, 15]], "sel": 9}`
- Error: logical-form mismatch

## test:12802:2-17716320-4

- Question: How much Goal Difference has less than 9 Losses, and 8 Draws, and more than 40 points?
- Gold: `{"sel": 9, "conds": [[6, 2, 9], [5, 0, 8], [3, 1, 40]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[6, 2, 9], [5, 0, 8], [3, 1, 40]], "sel": 9}`
- Error: logical-form mismatch

## test:12823:2-17817954-1

- Question: In 1979 when Jimmy Connors was the runner-up what was the score?
- Gold: `{"sel": 4, "conds": [[3, 0, "jimmy connors"], [1, 2, 1979]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, 1979], [3, 0, "Jimmy Connors"]], "sel": 4}`
- Error: logical-form mismatch

## test:12826:2-17817954-1

- Question: When Ilie Năstase beat runner-up Peter Fleming what year was it?
- Gold: `{"sel": 1, "conds": [[2, 0, "ilie năstase"], [3, 0, "peter fleming"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Ilie Năstase"], [3, 0, "Peter Fleming"]], "sel": 1}`
- Error: logical-form mismatch

## test:12832:2-18268890-5

- Question: What is the total pick number of player curt bennett from canada with a draft before 1976 and a round less than 2?
- Gold: `{"sel": 2, "conds": [[4, 0, "canada"], [0, 2, 1976], [3, 0, "curt bennett"], [1, 2, 2]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[3, 0, "curt bennett"], [4, 0, "canada"], [0, 2, 1976], [1, 2, 2]], "sel": 2}`
- Error: logical-form mismatch

## test:12857:2-18284277-1

- Question: What's the total time for the summer universiade competition?
- Gold: `{"sel": 5, "conds": [[1, 0, "summer universiade"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "summer universiade"]], "sel": 5}`
- Error: logical-form mismatch

## test:12862:2-178745-3

- Question: How many silver medals were won by the participant(s) that had more than 12 gold medals and 11 bronze medals?
- Gold: `{"sel": 2, "conds": [[1, 1, 12], [3, 0, 11]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 1, 12], [3, 0, 11]], "sel": 2}`
- Error: logical-form mismatch

## test:12868:2-18032715-8

- Question: How many specimens does the SANT institution have?
- Gold: `{"sel": 1, "conds": [[2, 0, "sant"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "SANT"]], "sel": 1}`
- Error: logical-form mismatch

## test:12897:2-18324411-4

- Question: In which area was there a score of 68?
- Gold: `{"sel": 0, "conds": [[3, 0, 68]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, 68]], "sel": 2}`
- Error: logical-form mismatch

## test:12905:2-178389-1

- Question: what is the year built of  kyrkjebø?
- Gold: `{"sel": 3, "conds": [[1, 0, "kyrkjebø"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "Kyrkjebø"]], "sel": 3}`
- Error: logical-form mismatch

## test:12909:2-18007222-1

- Question: What is the Total for the Player who won in 1922, 1932?
- Gold: `{"sel": 3, "conds": [[2, 0, "1922, 1932"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "1922 , 1932"]], "sel": 3}`
- Error: logical-form mismatch

## test:12910:2-18007222-1

- Question: What is the Total for the Player who won in 1936?
- Gold: `{"sel": 3, "conds": [[2, 0, "1936"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "1936"]], "sel": 3}`
- Error: logical-form mismatch

## test:12913:2-17876929-1

- Question: What is the number of points when goals were 29–30?
- Gold: `{"sel": 3, "conds": [[2, 0, "29–30"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "29–30"]], "sel": 3}`
- Error: logical-form mismatch

## test:12941:2-18295097-1

- Question: Which Elector has a Title of s. cecilia?
- Gold: `{"sel": 0, "conds": [[3, 0, "title of s. cecilia"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "s. cecilia"]], "sel": 0}`
- Error: logical-form mismatch

## test:12947:2-17747473-1

- Question: How many foundeds have stade tunisien as the club, with a capacity greater than 18,000?
- Gold: `{"sel": 2, "conds": [[0, 0, "stade tunisien"], [4, 1, "18,000"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "Stade Tunisien"], [4, 1, "18,000"]], "sel": 2}`
- Error: logical-form mismatch

## test:12948:2-17747473-1

- Question: How much capacity has 1944 as the founded?
- Gold: `{"sel": 4, "conds": [[2, 0, 1944]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, 1944]], "sel": 4}`
- Error: logical-form mismatch

## test:12961:2-18096431-3

- Question: Which To par has a Player of jack nicklaus, and a Total smaller than 146?
- Gold: `{"sel": 4, "conds": [[0, 0, "jack nicklaus"], [3, 2, 146]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "jack nicklaus"], [3, 2, 146]], "sel": 4}`
- Error: logical-form mismatch

## test:12985:2-17829169-2

- Question: What is the rank for total less than 5, 1 bronze and less than 1 silver?
- Gold: `{"sel": 0, "conds": [[4, 2, 5], [3, 0, 1], [2, 2, 1]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 2, 5], [3, 0, 1], [2, 2, 1]], "sel": 0}`
- Error: logical-form mismatch

## test:12997:2-18138953-3

- Question: What is the amount of money with a score of 67-71-70-71=279?
- Gold: `{"sel": 5, "conds": [[3, 0, "67-71-70-71=279"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "67-71-70-71=279"]], "sel": 5}`
- Error: logical-form mismatch

## test:13031:2-17857470-3

- Question: What party established in 1797 won an election in 2007?
- Gold: `{"sel": 4, "conds": [[2, 1, 1797], [5, 0, 2007]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, 1797], [5, 0, 2007]], "sel": 4}`
- Error: logical-form mismatch

## test:13033:2-18243389-9

- Question: What Played has a Lost smaller than 3, and a Drawn smaller than 0?
- Gold: `{"sel": 0, "conds": [[2, 2, 3], [1, 2, 0]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 2, 3], [1, 2, 0]], "sel": 0}`
- Error: logical-form mismatch

## test:13037:2-18243389-9

- Question: What is the Lost with Against smaller than 25, and Played smaller than 1?
- Gold: `{"sel": 2, "conds": [[3, 2, 25], [0, 2, 1]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[3, 2, 25], [0, 2, 1]], "sel": 2}`
- Error: logical-form mismatch

## test:13040:2-17751827-1

- Question: Name the team with a tie number of 6.
- Gold: `{"sel": 4, "conds": [[0, 0, "6"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "6"]], "sel": 1}`
- Error: logical-form mismatch

## test:13049:2-1772230-1

- Question: Which Population has a County of mississippi, and a Number of households smaller than 17,741?
- Gold: `{"sel": 4, "conds": [[0, 0, "mississippi"], [5, 2, "17,741"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "mississippi"], [5, 2, "17,741"]], "sel": 4}`
- Error: logical-form mismatch

## test:13050:2-18228282-7

- Question: Count the average Height which has a Position of pf, and a Year born (Age) on april 1, 1981 (age32)?
- Gold: `{"sel": 1, "conds": [[2, 0, "pf"], [3, 0, "april 1, 1981 (age32)"]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "pf"], [3, 0, "april 1, 1981 (age32)"]], "sel": 1}`
- Error: logical-form mismatch

## test:13052:2-17968303-5

- Question: Which 2005–06 Pts has a Team of estudiantes (lp), and a 2006–07 Pts smaller than 81?
- Gold: `{"sel": 1, "conds": [[0, 0, "estudiantes (lp)"], [2, 2, 81]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Estudiantes (LP)"], [2, 2, 81]], "sel": 1}`
- Error: logical-form mismatch

## test:13053:2-17968303-5

- Question: Which 2006–07 Pts has a 2005–06 Pts smaller than 51, a Team of huracán, and a 2007–08 Pts larger than 52?
- Gold: `{"sel": 2, "conds": [[1, 2, 51], [0, 0, "huracán"], [3, 1, 52]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 2, 51], [0, 0, "Huracán"], [3, 1, 52]], "sel": 2}`
- Error: logical-form mismatch

## test:13054:2-17968303-5

- Question: Which 2007–08 Pts has a Total Pts smaller than 173, a Total Pld larger than 38, a Team of banfield, and a 2005–06 Pts smaller than 59?
- Gold: `{"sel": 3, "conds": [[4, 2, 173], [5, 1, 38], [0, 0, "banfield"], [1, 2, 59]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[4, 2, 173], [5, 1, 38], [0, 0, "banfield"], [1, 2, 59]], "sel": 3}`
- Error: logical-form mismatch

## test:13055:2-17968303-5

- Question: Which 2006–07 Pts has a 2007–08 Pts of 53, and a 2005–06 Pts larger than 51?
- Gold: `{"sel": 2, "conds": [[3, 0, 53], [1, 1, 51]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[3, 0, 53], [1, 1, 51]], "sel": 2}`
- Error: logical-form mismatch

## test:13056:2-18229846-1

- Question: What is the map reference number for Lake Superior with a larger population than 65,216
- Gold: `{"sel": 1, "conds": [[4, 0, "lake superior"], [3, 1, "65,216"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "Lake Superior"], [3, 1, 65216]], "sel": 1}`
- Error: logical-form mismatch

## test:13058:2-18229846-1

- Question: What is the lowest rank with a smaller population in 2007 than 117,201 and whose map reference number is 22?
- Gold: `{"sel": 0, "conds": [[3, 1, "117,201"], [1, 0, 22]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[3, 2, "117,201"], [1, 0, 22]], "sel": 0}`
- Error: logical-form mismatch

## test:13063:2-18066655-1

- Question: What rank is He Yingqin who was born before 1890?
- Gold: `{"sel": 0, "conds": [[1, 0, "he yingqin"], [3, 2, 1890]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "He Yingqin"], [3, 2, 1890]], "sel": 0}`
- Error: logical-form mismatch

## test:13099:2-18018248-1

- Question: How many games have been played when there are 13 wins and 45 goals were conceded?
- Gold: `{"sel": 2, "conds": [[3, 0, 13], [7, 0, 45]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, 13], [7, 0, 45]], "sel": 2}`
- Error: logical-form mismatch

## test:13125:2-17902603-2

- Question: Whate place has 18 points with lost less than 8?
- Gold: `{"sel": 0, "conds": [[7, 0, 18], [4, 2, 8]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[7, 0, 18], [4, 2, 8]], "sel": 0}`
- Error: logical-form mismatch

## test:13129:2-17902603-2

- Question: When goals scored is more than 18, draw is less than 4, and goals conceded is more than 24, what is the sum of played?
- Gold: `{"sel": 2, "conds": [[5, 1, 18], [3, 2, 4], [6, 1, 24]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[5, 1, 18], [3, 2, 4], [6, 1, 24]], "sel": 2}`
- Error: logical-form mismatch

## test:13132:2-18164300-3

- Question: What is the total rank for the Netherlands when more than 2 silver medals were won?
- Gold: `{"sel": 0, "conds": [[1, 0, "netherlands"], [3, 1, 2]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "Netherlands"], [3, 1, 2]], "sel": 0}`
- Error: logical-form mismatch

## test:13133:2-18164300-3

- Question: What is the total medal count when there are more than 1 gold and more than 2 silver medals won and the rank is less than 1?
- Gold: `{"sel": 5, "conds": [[2, 1, 1], [3, 1, 2], [0, 2, 2]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[2, 1, 1], [3, 1, 2], [0, 2, 1]], "sel": 5}`
- Error: logical-form mismatch

## test:13160:2-17716055-1

- Question: Which Goals For has a Team of congleton town, and a Lost larger than 11?
- Gold: `{"sel": 5, "conds": [[1, 0, "congleton town"], [4, 1, 11]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "congleton town"], [4, 1, 11]], "sel": 5}`
- Error: logical-form mismatch

## test:13197:2-17747471-2

- Question: How many Points have Goals against of 35, and less than 13 losses?
- Gold: `{"sel": 3, "conds": [[8, 0, 35], [6, 2, 13]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[8, 0, 35], [6, 2, 13]], "sel": 3}`
- Error: logical-form mismatch

## test:13198:2-17747471-2

- Question: How many points have Goals for smaller than 33, and Draws larger than 9?
- Gold: `{"sel": 3, "conds": [[7, 2, 33], [5, 1, 9]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[7, 2, 33], [5, 1, 9]], "sel": 3}`
- Error: logical-form mismatch

## test:13199:2-17747471-2

- Question: Which Goal Difference has 13 Wins, and a Position of 3, and Played smaller than 30?
- Gold: `{"sel": 9, "conds": [[4, 0, 13], [0, 0, 3], [2, 2, 30]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 0, 13], [0, 0, 3], [2, 2, 30]], "sel": 9}`
- Error: logical-form mismatch

## test:13216:2-18187087-1

- Question: What is the total population of the district of Klang, with an area larger than 636?
- Gold: `{"sel": 2, "conds": [[1, 0, "klang"], [3, 1, 636]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "Klang"], [3, 1, 636]], "sel": 2}`
- Error: logical-form mismatch

## test:13236:2-176533-1

- Question: With an Area km 2 of less than 130.68, what is McAdam's Population?
- Gold: `{"sel": 3, "conds": [[2, 2, 130.68], [0, 0, "mcadam"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 2, 130.68], [0, 0, "McAdam"]], "sel": 3}`
- Error: logical-form mismatch

## test:13240:2-18337310-2

- Question: What is the total number of Round with a Method of submission (ankle lock), a Location of tokyo, japan, and a Record of 13-5-2?
- Gold: `{"sel": 4, "conds": [[3, 0, "submission (ankle lock)"], [6, 0, "tokyo, japan"], [1, 0, "13-5-2"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "submission (ankle lock)"], [6, 0, "tokyo, japan"], [1, 0, "13-5-2"]], "sel": 4}`
- Error: logical-form mismatch

## test:13243:2-17841851-1

- Question: Which Gold has a Nation of south korea (kor), and Bronze smaller than 65?
- Gold: `{"sel": 2, "conds": [[1, 0, "south korea (kor)"], [4, 2, 65]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "south korea (kor)"], [4, 2, 65]], "sel": 2}`
- Error: logical-form mismatch

## test:13254:2-18018214-3

- Question: which Points has Wins smaller than 2?
- Gold: `{"sel": 8, "conds": [[3, 2, 2]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[3, 2, 2]], "sel": 8}`
- Error: logical-form mismatch

## test:13256:2-18018214-3

- Question: Which Games played has a Points of 6, and Goals scored larger than 12?
- Gold: `{"sel": 2, "conds": [[8, 0, 6], [6, 1, 12]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[8, 0, 6], [6, 1, 12]], "sel": 2}`
- Error: logical-form mismatch

## test:13257:2-18018214-3

- Question: Which Goals scored has Points larger than 26 and Wins larger than 11?
- Gold: `{"sel": 6, "conds": [[8, 1, 26], [3, 1, 11]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[8, 1, 26], [3, 1, 11]], "sel": 6}`
- Error: logical-form mismatch

## test:13258:2-18018214-3

- Question: Which Loses has Points smaller than 6?
- Gold: `{"sel": 5, "conds": [[8, 2, 6]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[8, 2, 6]], "sel": 5}`
- Error: logical-form mismatch

## test:13259:2-18018214-3

- Question: Which Goals conceded has Points of 6 and Draws larger than 0?
- Gold: `{"sel": 7, "conds": [[8, 0, 6], [4, 1, 0]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[8, 0, 6], [4, 1, 0]], "sel": 7}`
- Error: logical-form mismatch

## test:13261:2-1829476-3

- Question: What is the total number of Wickets with a 26.13 average?
- Gold: `{"sel": 2, "conds": [[3, 0, 26.13]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, 26.13]], "sel": 2}`
- Error: logical-form mismatch

## test:13279:2-18980847-2

- Question: Which Goals have Apps smaller than 1?
- Gold: `{"sel": 4, "conds": [[3, 2, 1]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[3, 2, 1]], "sel": 4}`
- Error: logical-form mismatch

## test:13281:2-18980847-2

- Question: How many Goals have a National team of england, and Apps smaller than 6, and a Year of 2012?
- Gold: `{"sel": 4, "conds": [[0, 0, "england"], [3, 2, 6], [2, 0, "2012"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "england"], [3, 2, 6], [2, 0, "2012"]], "sel": 4}`
- Error: logical-form mismatch

## test:13286:2-18553832-4

- Question: How many bronzes had a rank of 10 and 0 gold?
- Gold: `{"sel": 4, "conds": [[0, 0, "10"], [2, 2, 0]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "10"], [2, 0, 0]], "sel": 4}`
- Error: logical-form mismatch

## test:13287:2-18553832-4

- Question: Hold many gold had more than 16 bronzes?
- Gold: `{"sel": 2, "conds": [[4, 1, 16]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 1, 16]], "sel": 2}`
- Error: logical-form mismatch

## test:13294:2-18901519-1

- Question: Which Bronze has a Silver of 15, and a Total smaller than 54?
- Gold: `{"sel": 4, "conds": [[3, 0, 15], [5, 2, 54]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[3, 0, 15], [5, 2, 54]], "sel": 4}`
- Error: logical-form mismatch

## test:13295:2-18901519-1

- Question: How many Bronzes have a Rank of 9, and a Silver larger than 2?
- Gold: `{"sel": 4, "conds": [[0, 0, "9"], [3, 1, 2]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "9"], [3, 1, 2]], "sel": 4}`
- Error: logical-form mismatch

## test:13302:2-18812438-1

- Question: Which Total Goals have a League Cup Goals larger than 0, and FA Cup Goals larger than 0?
- Gold: `{"sel": 9, "conds": [[7, 1, 0], [5, 1, 0]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[7, 1, 0], [5, 1, 0]], "sel": 9}`
- Error: logical-form mismatch

## test:13303:2-18812438-1

- Question: Which Total Goals have Total Apps of 42 (3), and League Goals smaller than 1?
- Gold: `{"sel": 9, "conds": [[8, 0, "42 (3)"], [3, 2, 1]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[8, 0, "42 (3)"], [3, 2, 1]], "sel": 9}`
- Error: logical-form mismatch

## test:13310:2-18737756-2

- Question: Which IHSAA class A school are the Cavaliers from?
- Gold: `{"sel": 4, "conds": [[3, 0, "a"], [2, 0, "cavaliers"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "A"], [2, 0, "Cavaliers"]], "sel": 0}`
- Error: logical-form mismatch

## test:13318:2-18384663-1

- Question: Which one was built in 2006 on the vessel named mf ørland?
- Gold: `{"sel": 4, "conds": [[2, 0, 2006], [0, 0, "mf ørland"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, 2006], [0, 0, "mf ørland"]], "sel": 1}`
- Error: logical-form mismatch

## test:13340:2-19001916-2

- Question: Which Power (MW) has a Voltage (kV) of 500, and a Country of argentina?
- Gold: `{"sel": 4, "conds": [[3, 0, 500], [1, 0, "argentina"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[3, 0, 500], [1, 0, "argentina"]], "sel": 4}`
- Error: logical-form mismatch

## test:13341:2-19001916-2

- Question: How much Voltage (kV) has a Country of argentina, and a Power (MW) larger than 30, and a Supply point of yacyretá?
- Gold: `{"sel": 3, "conds": [[1, 0, "argentina"], [4, 1, 30], [2, 0, "yacyretá"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "argentina"], [4, 1, 30], [2, 0, "yacyretá"]], "sel": 3}`
- Error: logical-form mismatch

## test:13352:2-18625461-5

- Question: What is Meagen Nay's rank with a lane greater than 5?
- Gold: `{"sel": 0, "conds": [[2, 0, "meagen nay"], [1, 1, 5]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Meagen Nay"], [1, 1, 5]], "sel": 0}`
- Error: logical-form mismatch

## test:13375:2-18600760-2

- Question: what is the latitude for the berlin township with a geo id less than 3801706260
- Gold: `{"sel": 5, "conds": [[0, 0, "berlin"], [7, 2, 3801706260]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Berlin"], [7, 2, 3801706260]], "sel": 5}`
- Error: logical-form mismatch

## test:13394:2-18830507-4

- Question: What is the sum rating with more than 1 comp for mark miller?
- Gold: `{"sel": 4, "conds": [[0, 0, "mark miller"], [2, 1, 1]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[2, 1, 1], [0, 0, "mark miller"]], "sel": 4}`
- Error: logical-form mismatch

## test:13412:2-18616766-3

- Question: Who received 6,131 televotes?
- Gold: `{"sel": 2, "conds": [[1, 0, "6,131"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "6,131"]], "sel": 0}`
- Error: logical-form mismatch

## test:13414:2-185274-1

- Question: What is the draw for the artist Ketil Stokkan which has less than 44 points?
- Gold: `{"sel": 0, "conds": [[2, 0, "ketil stokkan"], [6, 2, 44]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Ketil Stokkan"], [6, 2, 44]], "sel": 0}`
- Error: logical-form mismatch

## test:13431:2-1859-1

- Question: Which 2012 has a 2009 smaller than 3.38?
- Gold: `{"sel": 0, "conds": [[3, 2, 3.38]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[3, 2, 3.38]], "sel": 0}`
- Error: logical-form mismatch

## test:13432:2-1859-1

- Question: Which 2009 has a 2012 larger than 9,265?
- Gold: `{"sel": 3, "conds": [[0, 1, "9,265"]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[0, 1, 9265]], "sel": 3}`
- Error: logical-form mismatch

## test:13433:2-1859-1

- Question: Which 2012 has a 2008 of 24,473, and a 2009 smaller than 25,616?
- Gold: `{"sel": 0, "conds": [[4, 0, "24,473"], [3, 2, "25,616"]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "24,473"], [3, 2, "25,616"]], "sel": 0}`
- Error: logical-form mismatch

## test:13434:2-1859-1

- Question: Which 2010 has a 2008 larger than 3.41, and a 2009 smaller than 9,344, and a 2011 smaller than 26,452, and a 2012 smaller than 87.9?
- Gold: `{"sel": 2, "conds": [[4, 1, 3.41], [3, 2, "9,344"], [1, 2, "26,452"], [0, 2, 87.9]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[4, 1, 3.41], [3, 2, "9,344"], [1, 2, "26,452"], [0, 2, 87.9]], "sel": 2}`
- Error: logical-form mismatch

## test:13435:2-1859-1

- Question: How much 2012 has a 2011 smaller than 26,452, and a 2009 larger than 3.38, and a 2008 smaller than 90.3?
- Gold: `{"sel": 0, "conds": [[1, 2, "26,452"], [3, 1, 3.38], [4, 2, 90.3]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 2, "26,452"], [3, 1, "3.38"], [4, 2, "90.3"]], "sel": 0}`
- Error: logical-form mismatch

## test:13436:2-18828487-1

- Question: who is the champion when the year is earlier than 2012, the runner-up (average in final) is steve beaton (97.16)?
- Gold: `{"sel": 6, "conds": [[0, 2, 2012], [3, 0, "steve beaton (97.16)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 2, 2012], [3, 0, "Steve Beaton (97.16)"]], "sel": 1}`
- Error: logical-form mismatch

## test:13470:2-18625276-3

- Question: What is the rank for Denmark?
- Gold: `{"sel": 0, "conds": [[4, 0, "denmark"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "Denmark"]], "sel": 0}`
- Error: logical-form mismatch

## test:13472:2-18428035-3

- Question: What season had the title "A Safe Place"?
- Gold: `{"sel": 1, "conds": [[2, 0, "\"a safe place\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "A Safe Place"]], "sel": 1}`
- Error: logical-form mismatch

## test:13473:2-18428035-3

- Question: What season was the episode "Solitary Confinement", written by Fiona Kelly?
- Gold: `{"sel": 1, "conds": [[4, 0, "fiona kelly"], [2, 0, "\"solitary confinement\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Solitary Confinement"], [4, 0, "Fiona Kelly"]], "sel": 1}`
- Error: logical-form mismatch

## test:13476:2-1893924-11

- Question: Which Goals have Games of 51, and a Debut year smaller than 1992?
- Gold: `{"sel": 3, "conds": [[2, 0, 51], [0, 2, 1992]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[2, 0, 51], [0, 2, 1992]], "sel": 3}`
- Error: logical-form mismatch

## test:13509:2-18984959-2

- Question: Which Average has a Tally of 2-12, and a Total larger than 18?
- Gold: `{"sel": 6, "conds": [[3, 0, "2-12"], [4, 1, 18]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "2-12"], [4, 1, 18]], "sel": 6}`
- Error: logical-form mismatch

## test:13518:2-18673152-1

- Question: What is the sum of wins and the sum of losses less than 4 for teams larger than 20?
- Gold: `{"sel": 2, "conds": [[3, 2, 4], [6, 1, 20]], "agg": 4}`
- Prediction: `{"agg": 4, "conds": [[3, 2, 4], [5, 1, 20]], "sel": 2}`
- Error: logical-form mismatch

## test:13526:2-18600760-23

- Question: what is the geo id when the land (sqmi) is less than 36.112, the latitude is more than 47.536618, the township is west bay and water (sqmi) is more than 0.209?
- Gold: `{"sel": 7, "conds": [[3, 2, 36.112], [5, 1, 47.536618], [0, 0, "west bay"], [4, 1, 0.209]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[3, 2, 36.112], [5, 1, 47.536618], [0, 0, "West Bay"], [4, 1, 0.209]], "sel": 7}`
- Error: logical-form mismatch

## test:13528:2-18600760-23

- Question: what is the longitude when the water (sqmi) is 0.317 and the ansi code is higher than 1759695?
- Gold: `{"sel": 6, "conds": [[4, 0, 0.317], [8, 1, 1759695]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "0.317"], [8, 1, 1759695]], "sel": 6}`
- Error: logical-form mismatch

## test:13532:2-18403356-1

- Question: what is the silver when the nation is syria (syr) and gold is more than 0?
- Gold: `{"sel": 3, "conds": [[1, 0, "syria (syr)"], [2, 1, 0]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Syria (SYR)"], [2, 1, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:13536:2-18876359-2

- Question: In what years did Salina Kosgei compete in Singapore?
- Gold: `{"sel": 0, "conds": [[2, 0, "singapore"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Singapore"]], "sel": 0}`
- Error: logical-form mismatch

## test:13538:2-18624623-3

- Question: What is the Heat of the 34 Rank swimmer with a Time of 49.49 or less?
- Gold: `{"sel": 1, "conds": [[0, 0, 34], [5, 2, 49.49]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 34], [5, 2, 49.49]], "sel": 1}`
- Error: logical-form mismatch

## test:13539:2-18624623-3

- Question: What is Dominik Meichtry's Time in Heat 7 or lower?
- Gold: `{"sel": 5, "conds": [[3, 0, "dominik meichtry"], [1, 2, 7]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Dominik Meichtry"], [1, 2, 8]], "sel": 5}`
- Error: logical-form mismatch

## test:13556:2-18896680-1

- Question: What's the total enrollment in 57 Noble having a # and AA as the IHSAA Class?
- Gold: `{"sel": 3, "conds": [[5, 0, "57 noble"], [4, 0, "aa"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[5, 0, "57 Noble"], [4, 0, "AA"]], "sel": 3}`
- Error: logical-form mismatch

## test:13565:2-18522916-1

- Question: How many total draws was played less than 18 with 11 losts?
- Gold: `{"sel": 3, "conds": [[4, 0, 11], [2, 2, 18]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 2, 18], [4, 0, 11]], "sel": 3}`
- Error: logical-form mismatch

## test:13566:2-18522916-1

- Question: What is the total goals scored with more than 11 points, 18 goals conceded, and played fewer than 18 times?
- Gold: `{"sel": 5, "conds": [[7, 1, 11], [6, 0, 18], [2, 2, 18]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[7, 1, 11], [6, 0, 18], [2, 2, 18]], "sel": 5}`
- Error: logical-form mismatch

## test:13585:2-1859485-5

- Question: How many times did Morgan win The Masters Tournament with fewer than 12 appearances?
- Gold: `{"sel": 1, "conds": [[0, 0, "masters tournament"], [5, 2, 12]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Masters Tournament"], [5, 2, 12]], "sel": 1}`
- Error: logical-form mismatch

## test:13586:2-18975610-5

- Question: What is the lowest losses for a team that has 0 draws, fewer than 4 wins, and no Byes?
- Gold: `{"sel": 3, "conds": [[4, 0, 0], [1, 2, 4], [2, 2, 0]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[4, 0, 0], [1, 2, 4], [2, 0, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:13606:2-18811509-3

- Question: What is the To par for the player that won in 2003, with a total larger than 145?
- Gold: `{"sel": 4, "conds": [[2, 0, "2003"], [3, 1, 145]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "2003"], [3, 1, 145]], "sel": 4}`
- Error: logical-form mismatch

## test:13611:2-1859914-1

- Question: What is the fewest tally for the game played at Vasil Levski National Stadium, Sofia, Bulgaria?
- Gold: `{"sel": 4, "conds": [[1, 0, "vasil levski national stadium, sofia, bulgaria"]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[1, 0, "Vasil Levski National Stadium , Sofia , Bulgaria"]], "sel": 4}`
- Error: logical-form mismatch

## test:13615:2-18625553-4

- Question: Swimmer Jiao Liuyang has what for the sum of lane?
- Gold: `{"sel": 1, "conds": [[2, 0, "jiao liuyang"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[2, 0, "Jiao Liuyang"]], "sel": 1}`
- Error: logical-form mismatch

## test:13633:2-18568417-4

- Question: Which Inhabitants have a Mayor of matteo renzi, and an Election larger than 2009?
- Gold: `{"sel": 1, "conds": [[2, 0, "matteo renzi"], [4, 1, 2009]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "matteo renzi"], [4, 1, 2009]], "sel": 1}`
- Error: logical-form mismatch

## test:13634:2-18568417-4

- Question: Which Inhabitants have a Party of democratic party, and a Municipality of florence, and an Election smaller than 2009?
- Gold: `{"sel": 1, "conds": [[3, 0, "democratic party"], [0, 0, "florence"], [4, 2, 2009]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "democratic party"], [0, 0, "florence"], [4, 2, 2009]], "sel": 1}`
- Error: logical-form mismatch

## test:13635:2-18933007-2

- Question: Which Seatshave a Share of votes of 18%, and a Share of seats of 3%, and a General election smaller than 1992?
- Gold: `{"sel": 3, "conds": [[2, 0, "18%"], [4, 0, "3%"], [0, 2, 1992]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "18%"], [4, 0, "3%"], [0, 2, 1992]], "sel": 3}`
- Error: logical-form mismatch

## test:13637:2-18933007-2

- Question: Which Seats have a Share of votes of 18%, and a Share of seats of 3%, and a General election larger than 1992?
- Gold: `{"sel": 3, "conds": [[2, 0, "18%"], [4, 0, "3%"], [0, 1, 1992]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "18%"], [4, 0, "3%"], [0, 1, 1992]], "sel": 3}`
- Error: logical-form mismatch

## test:13649:2-18976008-1

- Question: How many Premierships have Nicknamed of kangaroos?
- Gold: `{"sel": 3, "conds": [[1, 0, "kangaroos"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "kangaroos"]], "sel": 3}`
- Error: logical-form mismatch

## test:13658:2-18430895-1

- Question: What year had the category of best international newcomer?
- Gold: `{"sel": 0, "conds": [[3, 0, "best international newcomer"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "best international newcomer"]], "sel": 0}`
- Error: logical-form mismatch

## test:13665:2-18974130-3

- Question: How many byes were there recorded with 0 draws?
- Gold: `{"sel": 2, "conds": [[4, 2, 0]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[4, 0, 0]], "sel": 2}`
- Error: logical-form mismatch

## test:13666:2-18974130-3

- Question: How many draws occured with a record of 10 losses, and 6 wins?
- Gold: `{"sel": 4, "conds": [[3, 0, 10], [1, 1, 6]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[3, 0, 10], [1, 0, 6]], "sel": 4}`
- Error: logical-form mismatch

## test:13667:2-18974130-3

- Question: How many byes were there with an Against of 1655 and more than 10 wins?
- Gold: `{"sel": 2, "conds": [[5, 0, 1655], [1, 1, 10]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[5, 0, 1655], [1, 1, 10]], "sel": 2}`
- Error: logical-form mismatch

## test:13668:2-18974130-3

- Question: What was the against were there were less than 3 byes?
- Gold: `{"sel": 5, "conds": [[2, 2, 3]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 2, 3]], "sel": 5}`
- Error: logical-form mismatch

## test:13678:2-18802322-1

- Question: How many years have claudia beni as the artist?
- Gold: `{"sel": 0, "conds": [[2, 0, "claudia beni"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "claudia beni"]], "sel": 0}`
- Error: logical-form mismatch

## test:13695:2-18666566-2

- Question: Which Rank has a Heat larger than 7?
- Gold: `{"sel": 0, "conds": [[1, 1, 7]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[1, 1, 7]], "sel": 0}`
- Error: logical-form mismatch

## test:13696:2-18666566-2

- Question: Which Heat has a Nation of australia, and a Rank larger than 7?
- Gold: `{"sel": 1, "conds": [[3, 0, "australia"], [0, 1, 7]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "australia"], [0, 1, 7]], "sel": 1}`
- Error: logical-form mismatch

## test:13698:2-18812209-19

- Question: What is the number of wins associated with 1 point, more than 1 start, and under 7 finishes?
- Gold: `{"sel": 3, "conds": [[2, 2, 7], [1, 1, 1], [6, 0, 1]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[6, 0, 1], [1, 1, 1], [2, 2, 7]], "sel": 3}`
- Error: logical-form mismatch

## test:13699:2-18812209-19

- Question: What is the number of finishes associated with 13 starts, more than 169 points, and 96 stage wins?
- Gold: `{"sel": 2, "conds": [[1, 0, 13], [6, 1, 169], [5, 0, 96]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 0, 13], [6, 1, 169], [5, 0, 96]], "sel": 2}`
- Error: logical-form mismatch

## test:13723:2-18569021-6

- Question: Which Lane has a Reaction Time smaller than 0.199, and a Country of united states, and a Name of muna lee, and a Time larger than 22.01?
- Gold: `{"sel": 0, "conds": [[3, 2, 0.199], [2, 0, "united states"], [1, 0, "muna lee"], [4, 1, 22.01]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[3, 2, 0.199], [2, 0, "united states"], [1, 0, "muna lee"], [4, 1, 22.01]], "sel": 0}`
- Error: logical-form mismatch

## test:13724:2-18569021-6

- Question: How many Lanes have a Country of jamaica, and a Name of kerron stewart, and a Time larger than 22?
- Gold: `{"sel": 0, "conds": [[2, 0, "jamaica"], [1, 0, "kerron stewart"], [4, 1, 22]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "jamaica"], [1, 0, "kerron stewart"], [4, 1, 22]], "sel": 0}`
- Error: logical-form mismatch

## test:13726:2-18569021-6

- Question: Which Lane has a Country of united states, and a Time smaller than 22.01, and a Reaction Time smaller than 0.193?
- Gold: `{"sel": 0, "conds": [[2, 0, "united states"], [4, 2, 22.01], [3, 2, 0.193]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "united states"], [4, 2, 22.01], [3, 2, 0.193]], "sel": 0}`
- Error: logical-form mismatch

## test:13736:2-18639024-5

- Question: What's the total of the 2012-13 season when they're ranked 1st, a high more than 31,884 and an average more than 15,234?
- Gold: `{"sel": 3, "conds": [[4, 0, "1st"], [1, 1, "31,884"], [2, 1, "15,234"], [0, 0, "2012-13 season"]], "agg": 0}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "2012-13 season"], [4, 0, "1st"], [1, 1, "31,884"], [2, 1, "15,234"]], "sel": 3}`
- Error: logical-form mismatch

## test:13752:2-18639024-10

- Question: Which player from A-League 39 (110) has the highest games per goal?
- Gold: `{"sel": 5, "conds": [[2, 0, "39 (110)"]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "39 (110)"], [5, 0, 2.72]], "sel": 0}`
- Error: logical-form mismatch

## test:13755:2-18769869-2

- Question: What's the week when the result was W 38-24 and attendance was less than 43,449?
- Gold: `{"sel": 0, "conds": [[3, 0, "w 38-24"], [4, 2, "43,449"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "W 38-24"], [4, 2, "43,449"]], "sel": 0}`
- Error: logical-form mismatch

## test:13756:2-18769869-2

- Question: What's the week when the Green Bay Packers were the opponent and less than 57,966 were in attendance?
- Gold: `{"sel": 0, "conds": [[4, 2, "57,966"], [2, 0, "green bay packers"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "green bay packers"], [4, 2, 57966]], "sel": 0}`
- Error: logical-form mismatch

## test:13769:2-18427769-1

- Question: With the title "Memories by Moonlight", and a less than 39 number in season, and a greater than 66 number in series, who was the written by?
- Gold: `{"sel": 4, "conds": [[0, 1, 66], [1, 2, 39], [2, 0, "\"memories by moonlight\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Memories by Moonlight"], [1, 2, 39], [0, 1, 66]], "sel": 4}`
- Error: logical-form mismatch

## test:13770:2-18427769-1

- Question: Who directed the episode that was greater than 74 in the series, and had "Life Class" as the title?
- Gold: `{"sel": 3, "conds": [[0, 1, 74], [2, 0, "\"life class\""]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 1, 74], [2, 0, "Life Class"]], "sel": 3}`
- Error: logical-form mismatch

## test:13773:2-18894139-4

- Question: What is the average total for countries with under 3 golds and 0 silvers?
- Gold: `{"sel": 5, "conds": [[2, 2, 3], [3, 2, 0]], "agg": 5}`
- Prediction: `{"agg": 5, "conds": [[2, 2, 3], [3, 0, 0]], "sel": 5}`
- Error: logical-form mismatch

## test:13781:2-18625276-4

- Question: What lane did Bronte Barratt, who had a rank larger than 4, swim in?
- Gold: `{"sel": 1, "conds": [[2, 0, "bronte barratt"], [0, 1, 4]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Bronte Barratt"], [0, 1, 4]], "sel": 1}`
- Error: logical-form mismatch

## test:13782:2-18625276-4

- Question: In which lane did the swimmer with a time of 1:58.44 swim?
- Gold: `{"sel": 1, "conds": [[4, 0, "1:58.44"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "1:58.44"]], "sel": 1}`
- Error: logical-form mismatch

## test:13799:2-18581415-1

- Question: What is the Population 1961 of West Sussex with a Population of 120,952 or less?
- Gold: `{"sel": 4, "conds": [[0, 0, "west sussex"], [2, 2, "120,952"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "West Sussex"], [2, 2, "120,952"]], "sel": 4}`
- Error: logical-form mismatch

## test:13804:2-1897000-1

- Question: How many Spectators have a Date of 17 june 2006, and a Time (CET) larger than 15?
- Gold: `{"sel": 4, "conds": [[0, 0, "17 june 2006"], [1, 1, 15]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "17 june 2006"], [1, 1, 15]], "sel": 4}`
- Error: logical-form mismatch

## test:13824:2-18463855-1

- Question: Which League Goals have FA Cup Apps of 2, and Total Goals smaller than 0?
- Gold: `{"sel": 3, "conds": [[4, 0, "2"], [9, 2, 0]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 0, 2], [9, 2, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:13864:2-18946749-4

- Question: Which Prominence (m) has a Rank of 10, and a Col (m) smaller than 50?
- Gold: `{"sel": 5, "conds": [[0, 0, 10], [6, 2, 50]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 10], [6, 2, 50]], "sel": 5}`
- Error: logical-form mismatch

## test:13865:2-18946749-4

- Question: Which Rank has a Prominence (m) of 1,798, and a Col (m) larger than 810?
- Gold: `{"sel": 0, "conds": [[5, 0, "1,798"], [6, 1, 810]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "1,798"], [6, 1, 810]], "sel": 0}`
- Error: logical-form mismatch

## test:13866:2-18946749-4

- Question: How much Prominence (m) has an Elevation (m) of 2,797, and a Col (m) smaller than 0?
- Gold: `{"sel": 5, "conds": [[4, 0, "2,797"], [6, 2, 0]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "2,797"], [6, 2, 0]], "sel": 5}`
- Error: logical-form mismatch

## test:13892:2-18454375-3

- Question: what is the heat when the nationality is australia and the rank is less than 1?
- Gold: `{"sel": 1, "conds": [[3, 0, "australia"], [0, 2, 1]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "australia"], [0, 2, 1]], "sel": 1}`
- Error: logical-form mismatch

## test:13893:2-18487274-1

- Question: What is the fewest Al Ahly wins for El Zamalek wins of 0 and 0 draws?
- Gold: `{"sel": 2, "conds": [[3, 0, 0], [4, 2, 0]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[4, 0, 0], [3, 0, 0]], "sel": 2}`
- Error: logical-form mismatch

## test:13919:2-18811481-1

- Question: What is the Draw number of the song by Artist of "Loudest Whisper" with 68 or less Points with a place of 9 or larger?
- Gold: `{"sel": 0, "conds": [[3, 2, 68], [2, 0, "loudest whisper"], [4, 1, 9]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Loudest Whisper"], [3, 2, 68], [4, 1, 9]], "sel": 0}`
- Error: logical-form mismatch

## test:13920:2-18811481-1

- Question: What is the Place of the Song by Artist Rosie Hunter with a Draw of 1 or larger?
- Gold: `{"sel": 4, "conds": [[2, 0, "rosie hunter"], [0, 1, 1]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Rosie Hunter"], [0, 1, 1]], "sel": 4}`
- Error: logical-form mismatch

## test:13943:2-1900108-1

- Question: What is the value in 2010 for an airport ranked higher than 3 located in Cluj-Napoca?
- Gold: `{"sel": 5, "conds": [[2, 0, "cluj-napoca"], [0, 1, 3]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 1, 3], [2, 0, "Cluj-Napoca"]], "sel": 5}`
- Error: logical-form mismatch

## test:13944:2-1851063-10

- Question: What was the venue when David Jacobs was the host?
- Gold: `{"sel": 2, "conds": [[5, 0, "david jacobs"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "David Jacobs"]], "sel": 2}`
- Error: logical-form mismatch

## test:13969:2-18501840-1

- Question: What is the total number pick for seattle mariners team?
- Gold: `{"sel": 0, "conds": [[2, 0, "seattle mariners"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[2, 0, "seattle mariners"]], "sel": 0}`
- Error: logical-form mismatch

## test:13980:2-18602446-15

- Question: What is the result of Waldemar 27´s freestyle test?
- Gold: `{"sel": 4, "conds": [[2, 0, "waldemar 27"], [3, 0, "freestyle test"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Waldemar 27"], [3, 0, "Freestyle Test"]], "sel": 4}`
- Error: logical-form mismatch

## test:14006:2-18600121-5

- Question: Which 2008 has a City of durban?
- Gold: `{"sel": 3, "conds": [[2, 0, "durban"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "durban"]], "sel": 3}`
- Error: logical-form mismatch

## test:14008:2-18600121-5

- Question: Which 2008 has an Airport of hurghada international airport?
- Gold: `{"sel": 3, "conds": [[1, 0, "hurghada international airport"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "hurghada international airport"]], "sel": 3}`
- Error: logical-form mismatch

## test:14009:2-18600121-5

- Question: Which 2008 has an Airport of julius nyerere international airport?
- Gold: `{"sel": 3, "conds": [[1, 0, "julius nyerere international airport"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "julius nyerere international airport"]], "sel": 3}`
- Error: logical-form mismatch

## test:14013:2-184942-1

- Question: How many points does catcat have with more than 2 draws?
- Gold: `{"sel": 6, "conds": [[2, 0, "catcat"], [0, 1, 2]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "catcat"], [0, 1, 2]], "sel": 6}`
- Error: logical-form mismatch

## test:14018:2-18428024-3

- Question: What episode number in the series was "facing the music" that was episode number greater than 6 in the season?
- Gold: `{"sel": 0, "conds": [[2, 0, "\"facing the music\""], [1, 1, 6]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "facing the music"], [1, 1, 6]], "sel": 0}`
- Error: logical-form mismatch

## test:14019:2-18662643-17

- Question: What is the Rank of the Player with a Time of 7:20.32 and Notes of FB?
- Gold: `{"sel": 0, "conds": [[4, 0, "fb"], [3, 0, "7:20.32"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "7:20.32"], [4, 0, "FB"]], "sel": 0}`
- Error: logical-form mismatch

## test:14031:2-18567686-1

- Question: Which Opened has a System of c-train, and a Daily ridership smaller than 269,600?
- Gold: `{"sel": 5, "conds": [[1, 0, "c-train"], [3, 2, "269,600"]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "c-train"], [3, 2, 269600]], "sel": 5}`
- Error: logical-form mismatch

## test:14036:2-18594107-1

- Question: How many total games were played by the team which had a total of 16 points and less than 4 draws?
- Gold: `{"sel": 2, "conds": [[8, 0, 16], [4, 2, 4]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[8, 0, 16], [4, 2, 4]], "sel": 2}`
- Error: logical-form mismatch

## test:14038:2-18594107-1

- Question: How many points are in the scored category for the team that played less than 18 games?
- Gold: `{"sel": 6, "conds": [[2, 2, 18]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 2, 18]], "sel": 6}`
- Error: logical-form mismatch

## test:14039:2-18594107-1

- Question: How many points are in the scored category for the team that has 8 total points and a position that is less than 10?
- Gold: `{"sel": 6, "conds": [[8, 0, 8], [0, 2, 10]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[8, 0, 8], [0, 2, 10]], "sel": 6}`
- Error: logical-form mismatch

## test:14040:2-18594107-1

- Question: How many loses does the team have that conceded 25 and won more than 6 games?
- Gold: `{"sel": 5, "conds": [[7, 0, 25], [3, 1, 6]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[7, 0, 25], [3, 1, 6]], "sel": 5}`
- Error: logical-form mismatch

## test:14041:2-18594107-1

- Question: Out of the teams that have scored lower than 25 points, have a total of points less than 20, and a position larger than 8, which has the lowest amount of draws?
- Gold: `{"sel": 4, "conds": [[6, 2, 25], [8, 0, 20], [0, 1, 8]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[6, 2, 25], [8, 2, 20], [0, 1, 8]], "sel": 4}`
- Error: logical-form mismatch

## test:14042:2-18561357-2

- Question: How many bronze medals did the nation have that had less than 3 silver, 5 gold and ranked better than 31?
- Gold: `{"sel": 4, "conds": [[3, 2, 3], [0, 2, 31], [2, 0, 5]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[3, 2, 3], [2, 0, 5], [0, 2, 31]], "sel": 4}`
- Error: logical-form mismatch

## test:14052:2-18600760-9

- Question: How much Longitude has a County of nelson, and a Latitude larger than 47.980183?
- Gold: `{"sel": 6, "conds": [[1, 0, "nelson"], [5, 1, 47.980183]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Nelson"], [5, 1, 47.980183]], "sel": 6}`
- Error: logical-form mismatch

## test:14053:2-18600760-9

- Question: Which Water (sqmi) has a County of benson, and an ANSI code smaller than 1759243?
- Gold: `{"sel": 4, "conds": [[1, 0, "benson"], [8, 2, 1759243]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Benson"], [8, 2, 1759243]], "sel": 4}`
- Error: logical-form mismatch

## test:14054:2-18600760-9

- Question: Which Pop (2010) has an ANSI code smaller than 1036864, and a Longitude larger than -98.46611, and a Land (sqmi) smaller than 36.238, and a Latitude smaller than 48.144102?
- Gold: `{"sel": 2, "conds": [[8, 2, 1036864], [6, 1, -98.46611], [3, 2, 36.238], [5, 2, 48.144102]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[8, 2, 1036864], [6, 1, -98.46611], [3, 2, 36.238], [5, 2, 48.144102]], "sel": 2}`
- Error: logical-form mismatch

## test:14072:2-18416665-1

- Question: What was the Best Feature Film at the Macabro Film Festival?
- Gold: `{"sel": 4, "conds": [[0, 0, "best feature film"], [1, 0, "macabro film festival"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Best Feature Film"], [1, 0, "Macabro Film Festival"]], "sel": 2}`
- Error: logical-form mismatch

## test:14076:2-18382509-2

- Question: What is the sales when the artist is kelly clarkson?
- Gold: `{"sel": 4, "conds": [[1, 0, "kelly clarkson"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "kelly clarkson"]], "sel": 4}`
- Error: logical-form mismatch

## test:14085:2-18622103-2

- Question: What is the number of staterooms when guests was larger than 210?
- Gold: `{"sel": 6, "conds": [[5, 1, 210]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[5, 1, 210]], "sel": 6}`
- Error: logical-form mismatch

## test:14086:2-18622103-2

- Question: What is the number of guests for the Viking Ingvar, built earlier than 1990?
- Gold: `{"sel": 5, "conds": [[0, 0, "viking ingvar"], [1, 2, 1990]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Viking Ingvar"], [1, 2, 1990]], "sel": 5}`
- Error: logical-form mismatch

## test:14097:2-18616240-1

- Question: What was the earliest year for the 400 M Hurdles in Santiago, Chile?
- Gold: `{"sel": 0, "conds": [[2, 0, "santiago, chile"], [4, 0, "400 m hurdles"]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[4, 0, "400 m hurdles"], [2, 0, "Santiago , Chile"]], "sel": 0}`
- Error: logical-form mismatch

## test:14109:2-18941206-1

- Question: What is the IHSAA Class for a school in Munster with an enrollment of 1,206?
- Gold: `{"sel": 4, "conds": [[3, 1, "1,206"], [1, 0, "munster"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Munster"], [3, 0, 1206]], "sel": 4}`
- Error: logical-form mismatch

## test:14111:2-18941206-1

- Question: What is the enrollment for the school Highland?
- Gold: `{"sel": 3, "conds": [[0, 0, "highland"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Highland"]], "sel": 3}`
- Error: logical-form mismatch

## test:14133:2-18486567-2

- Question: What is the for the f136fb engine?
- Gold: `{"sel": 3, "conds": [[0, 0, "f136fb"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "f136fb"]], "sel": 1}`
- Error: logical-form mismatch

## test:14157:2-18495923-1

- Question: Which Number of electorates (2009) has a District of sheopur, and a Constituency number of 1?
- Gold: `{"sel": 4, "conds": [[3, 0, "sheopur"], [0, 0, "1"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "sheopur"], [0, 0, "1"]], "sel": 4}`
- Error: logical-form mismatch

## test:14162:2-1886358-1

- Question: How many Games have an Average smaller than 46,864, and a W-L-T of 2-3-0, and an Attendance smaller than 98,776, and a Season larger than 1958?
- Gold: `{"sel": 1, "conds": [[4, 2, "46,864"], [2, 0, "2-3-0"], [3, 2, "98,776"], [0, 1, 1958]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[4, 2, "46,864"], [2, 0, "2-3-0"], [3, 2, "98,776"], [0, 1, 1958]], "sel": 1}`
- Error: logical-form mismatch

## test:14163:2-1886358-1

- Question: How much Attendance has Games smaller than 6, and a W-L-T of 3-2-0, and a Season smaller than 1948?
- Gold: `{"sel": 3, "conds": [[1, 2, 6], [2, 0, "3-2-0"], [0, 2, 1948]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 2, 6], [2, 0, "3-2-0"], [0, 2, 1948]], "sel": 3}`
- Error: logical-form mismatch

## test:14219:2-18513028-1

- Question: What is the prize level when the Prize if Wrong is 1,000 and the question is less than 2?
- Gold: `{"sel": 1, "conds": [[4, 0, "1,000"], [0, 2, 2]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "1,000"], [0, 2, 2]], "sel": 1}`
- Error: logical-form mismatch

## test:14224:2-18938143-5

- Question: How many silver medals for germany with a bronze count more than 0?
- Gold: `{"sel": 3, "conds": [[1, 0, "germany"], [4, 1, 0]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Germany"], [4, 1, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:14225:2-18938143-5

- Question: How many gold medals when the total is more than 1 and 18 silver?
- Gold: `{"sel": 2, "conds": [[5, 1, 1], [3, 0, 18]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[5, 1, 1], [3, 0, 18]], "sel": 2}`
- Error: logical-form mismatch

## test:14226:2-18938143-5

- Question: How many bronze medals has a total less than 3 with a silver less than 1 and gold more than 1?
- Gold: `{"sel": 4, "conds": [[5, 2, 3], [3, 2, 1], [2, 1, 1]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[5, 2, 3], [3, 2, 1], [2, 1, 1]], "sel": 4}`
- Error: logical-form mismatch

## test:14233:2-18569335-2

- Question: How many heats did Runners from Guinea-Bissau run, with rank higher than 33?
- Gold: `{"sel": 1, "conds": [[3, 0, "guinea-bissau"], [0, 2, 33]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "Guinea-Bissau"], [0, 1, 33]], "sel": 1}`
- Error: logical-form mismatch

## test:14262:2-18672607-1

- Question: Which ISHAA school joined in 2012 and has a mascot of the panthers?
- Gold: `{"sel": 4, "conds": [[7, 2, 2012], [2, 0, "panthers"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[7, 0, 2012], [2, 0, "panthers"]], "sel": 0}`
- Error: logical-form mismatch

## test:14263:2-18479882-1

- Question: Which Tries against has Points against larger than 156, and Points for of 127, and Tries for larger than 17?
- Gold: `{"sel": 2, "conds": [[5, 1, 156], [4, 0, 127], [1, 1, 17]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[5, 1, 156], [4, 0, 127], [1, 1, 17]], "sel": 2}`
- Error: logical-form mismatch

## test:14275:2-18765877-1

- Question: Which round was the defensive tackle picked after 187?
- Gold: `{"sel": 0, "conds": [[3, 0, "defensive tackle"], [1, 1, 187]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 1, 187], [3, 0, "defensive tackle"]], "sel": 0}`
- Error: logical-form mismatch

## test:14285:2-1860425-1

- Question: what is the  Density (per km²) when the Area (km²) is 372,889 and the population (2011) is 1,145,861?
- Gold: `{"sel": 4, "conds": [[3, 0, "372,889"], [2, 1, "1,145,861"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "372,889"], [2, 0, "1,145,861"]], "sel": 4}`
- Error: logical-form mismatch

## test:14286:2-1860425-1

- Question: what is the area (km²) when the rank is south africa and the population (2011) is more than 51,770,561?
- Gold: `{"sel": 3, "conds": [[0, 0, "south africa"], [2, 1, "51,770,561"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "south africa"], [2, 1, "51,770,561"]], "sel": 3}`
- Error: logical-form mismatch

## test:14304:2-18826631-4

- Question: Name the Gold which has a Nation of australia, and a Bronze smaller than 1?
- Gold: `{"sel": 2, "conds": [[1, 0, "australia"], [4, 2, 1]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "australia"], [4, 2, 1]], "sel": 2}`
- Error: logical-form mismatch

## test:14318:2-18976447-3

- Question: What is the sum of Against values for teams with 5 losses and 0 draws?
- Gold: `{"sel": 5, "conds": [[3, 0, 5], [4, 2, 0]], "agg": 4}`
- Prediction: `{"agg": 4, "conds": [[3, 0, 5], [4, 0, 0]], "sel": 5}`
- Error: logical-form mismatch

## test:14326:2-18661293-4

- Question: How many silver medals when the total was 2 and less than 1 bronze?
- Gold: `{"sel": 3, "conds": [[4, 2, 1], [5, 0, 2]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[5, 0, 2], [4, 2, 1]], "sel": 3}`
- Error: logical-form mismatch

## test:14328:2-18661293-4

- Question: What's the gold medal count for Total Nation with a bronze count more than 0 and a total less than 54?
- Gold: `{"sel": 2, "conds": [[4, 1, 0], [1, 0, "total"], [5, 2, 54]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Total"], [4, 1, 0], [5, 2, 54]], "sel": 2}`
- Error: logical-form mismatch

## test:14356:2-12899300-6

- Question: What is the highest number of cuts made in a tournament with 0 wins and 0 top 5 placings?
- Gold: `{"sel": 5, "conds": [[2, 0, 0], [1, 2, 0]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[1, 0, 0], [2, 0, 0]], "sel": 5}`
- Error: logical-form mismatch

## test:14364:2-12379470-3

- Question: How many totals have brazil as the nation, and a bronze less than 2?
- Gold: `{"sel": 4, "conds": [[0, 0, "brazil"], [3, 2, 2]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "brazil"], [3, 2, 2]], "sel": 4}`
- Error: logical-form mismatch

## test:14365:2-12379470-3

- Question: How many silvers have 2 as gold, and a bronze less than 2?
- Gold: `{"sel": 2, "conds": [[1, 0, 2], [3, 2, 2]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[1, 0, 2], [3, 2, 2]], "sel": 2}`
- Error: logical-form mismatch

## test:14375:2-12161822-4

- Question: How many rounds have a Grand Prix of german gp?
- Gold: `{"sel": 0, "conds": [[2, 0, "german gp"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "German GP"]], "sel": 0}`
- Error: logical-form mismatch

## test:14388:2-12446342-4

- Question: With a time of 53.33, who ranked the highest?
- Gold: `{"sel": 0, "conds": [[4, 0, 53.33]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[4, 0, 53.33]], "sel": 2}`
- Error: logical-form mismatch

## test:14389:2-12446342-4

- Question: What was Great Britain's total time?
- Gold: `{"sel": 4, "conds": [[3, 0, "great britain"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[3, 0, "great britain"]], "sel": 4}`
- Error: logical-form mismatch

## test:14410:2-13105085-1

- Question: In which year did he finish 11th?
- Gold: `{"sel": 0, "conds": [[3, 0, "11th"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "11th"]], "sel": 0}`
- Error: logical-form mismatch

## test:14428:2-12877449-8

- Question: Which Championship total is over 13?
- Gold: `{"sel": 4, "conds": [[1, 1, 13]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 1, 13]], "sel": 1}`
- Error: logical-form mismatch

## test:14429:2-1302886-1

- Question: When Kerry is at 36.7%, what is the total number of others?
- Gold: `{"sel": 6, "conds": [[1, 0, "36.7%"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "36.7%"]], "sel": 6}`
- Error: logical-form mismatch

## test:14430:2-1302886-1

- Question: When Kerry has 70.2% and 1,439,724, what is the Bush#?
- Gold: `{"sel": 4, "conds": [[1, 0, "70.2%"], [2, 1, "1,439,724"]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "70.2%"], [2, 0, 1439724]], "sel": 4}`
- Error: logical-form mismatch

## test:14434:2-1262432-4

- Question: VIE is the IATA for which city?
- Gold: `{"sel": 5, "conds": [[3, 0, "vie"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "vie"]], "sel": 0}`
- Error: logical-form mismatch

## test:14449:2-12587230-1

- Question: What year has american music awards?
- Gold: `{"sel": 0, "conds": [[1, 0, "american music awards"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "american music awards"]], "sel": 0}`
- Error: logical-form mismatch

## test:14450:2-12587230-1

- Question: What was album of the year after 2009?
- Gold: `{"sel": 4, "conds": [[0, 1, 2009], [2, 0, "album of the year"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Album of the Year"], [0, 1, 2009]], "sel": 3}`
- Error: logical-form mismatch

## test:14451:2-12587230-1

- Question: How many years had ozone awards?
- Gold: `{"sel": 0, "conds": [[1, 0, "ozone awards"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "ozone awards"]], "sel": 0}`
- Error: logical-form mismatch

## test:14498:2-1228248-1

- Question: What is the number of points for the maserati straight-4 engine, later than 1959?
- Gold: `{"sel": 4, "conds": [[3, 0, "maserati straight-4"], [0, 1, 1959]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "maserati straight-4"], [0, 1, 1959]], "sel": 4}`
- Error: logical-form mismatch

## test:14505:2-12755231-1

- Question: What is the height of the fort peck dam which was built before 1968, is located in the united states and has a dam type of TE ?
- Gold: `{"sel": 3, "conds": [[2, 2, 1968], [6, 0, "te"], [1, 0, "united states"], [0, 0, "fort peck dam"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 2, 1968], [1, 0, "united states"], [6, 0, "TE"]], "sel": 3}`
- Error: logical-form mismatch

## test:14523:2-12382684-1

- Question: What is the sum of total with a Rank larger than 12, and a Gold larger than 4?
- Gold: `{"sel": 5, "conds": [[0, 1, 12], [2, 1, 4]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[0, 1, 12], [2, 1, 4]], "sel": 5}`
- Error: logical-form mismatch

## test:14527:2-12382684-1

- Question: What is the total rank with a Nation of gotland, and a Gold larger than 23?
- Gold: `{"sel": 0, "conds": [[1, 0, "gotland"], [2, 1, 23]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "gotland"], [2, 1, 23]], "sel": 0}`
- Error: logical-form mismatch

## test:14528:2-12317436-1

- Question: for a Goals Against greater than 42 what is the number of losses?
- Gold: `{"sel": 3, "conds": [[6, 1, 42]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[6, 1, 42]], "sel": 3}`
- Error: logical-form mismatch

## test:14529:2-12317436-1

- Question: for goals less than 48 and 8 games played what is the count of losses?
- Gold: `{"sel": 3, "conds": [[1, 0, 8], [5, 2, 48]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[5, 2, 48], [1, 0, 8]], "sel": 3}`
- Error: logical-form mismatch

## test:14541:2-13149986-2

- Question: Bronze larger than 2, and a Rank of 4, and a Total larger than 7 has how many numbers of gold?
- Gold: `{"sel": 1, "conds": [[3, 1, 2], [0, 0, 4], [4, 1, 7]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[3, 1, 2], [0, 0, 4], [4, 1, 7]], "sel": 1}`
- Error: logical-form mismatch

## test:14554:2-12205709-5

- Question: On games against the Devil Rays and a score of 2 - 1 (10), what was the attendance?
- Gold: `{"sel": 4, "conds": [[1, 0, "devil rays"], [2, 0, "2 - 1 (10)"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Devil Rays"], [2, 0, "2 - 1 (10)"]], "sel": 4}`
- Error: logical-form mismatch

## test:14555:2-12205709-5

- Question: On the game that put the team at 34-44, what was the attendance?
- Gold: `{"sel": 4, "conds": [[5, 0, "34-44"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "34-44"]], "sel": 4}`
- Error: logical-form mismatch

## test:14556:2-12205709-5

- Question: What was the score of the game that put the team at 27-32?
- Gold: `{"sel": 3, "conds": [[5, 0, "27-32"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "27-32"]], "sel": 2}`
- Error: logical-form mismatch

## test:14564:2-1219572-1

- Question: What game, played on October 17 in front of 49,347 fans, had the lowest score?
- Gold: `{"sel": 0, "conds": [[1, 0, "october 17"], [5, 1, "49,347"]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[1, 0, "October 17"], [5, 0, "49,347"]], "sel": 0}`
- Error: logical-form mismatch

## test:14565:2-1247786-1

- Question: What is the highest Total Foreign-born (1000) from a non EU state (1000) of 685 and a population (1000) smaller than 10,666?
- Gold: `{"sel": 2, "conds": [[4, 0, 685], [1, 1, "10,666"]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[4, 0, "685"], [1, 2, "10,666"]], "sel": 2}`
- Error: logical-form mismatch

## test:14567:2-1247786-1

- Question: How many Foreign-born (1000) are from Sweden and born in some other EU state (1000) larger than 477?
- Gold: `{"sel": 2, "conds": [[0, 0, "sweden"], [3, 1, 477]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "sweden"], [3, 1, 477]], "sel": 2}`
- Error: logical-form mismatch

## test:14569:2-1247786-1

- Question: What is the greatest Born in other EU state (1000) with more than 1,380 foreign-born from Italy and a born in a non EU state (1000) less than 3,205?
- Gold: `{"sel": 3, "conds": [[2, 1, "1,380"], [0, 0, "italy"], [4, 2, "3,205"]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[2, 1, 1380], [4, 2, 3205]], "sel": 3}`
- Error: logical-form mismatch

## test:14576:2-13012881-1

- Question: How many sets were played in the tournament that had 4R in 2011 and 2R in 2008?
- Gold: `{"sel": 3, "conds": [[4, 0, "4r"], [2, 0, "2r"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "4R"], [2, 0, "2R"]], "sel": 0}`
- Error: logical-form mismatch

## test:14585:2-1235945-1

- Question: What is the total years with more than 1 points?
- Gold: `{"sel": 0, "conds": [[4, 1, 1]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[4, 1, 1]], "sel": 0}`
- Error: logical-form mismatch

## test:14587:2-12188532-6

- Question: Which home team has an Away of (2-1)?
- Gold: `{"sel": 2, "conds": [[3, 0, "(2-1)"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "(2-1)"]], "sel": 0}`
- Error: logical-form mismatch

## test:14591:2-12188532-6

- Question: Which team has an overall playoff of (0-0), a home record of (0-1) and played the Green Bay Blizzard team?
- Gold: `{"sel": 1, "conds": [[4, 0, "(0-0)"], [2, 0, "(0-1)"], [0, 0, "green bay blizzard"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "(0-0)"], [2, 0, "(0-1)"], [0, 0, "Green Bay Blizzard"]], "sel": 0}`
- Error: logical-form mismatch

## test:14616:2-13312898-50

- Question: Name the most pick # for overall of 204
- Gold: `{"sel": 1, "conds": [[2, 0, 204]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, 204]], "sel": 3}`
- Error: logical-form mismatch

## test:14620:2-1226512-2

- Question: What points did the ilmor v10 engine get after 1992?
- Gold: `{"sel": 4, "conds": [[3, 0, "ilmor v10"], [0, 1, 1992]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "Ilmor V10"], [0, 1, 1992]], "sel": 4}`
- Error: logical-form mismatch

## test:14626:2-13023925-2

- Question: What was the record after the game against the St. Louis Cardinals?
- Gold: `{"sel": 5, "conds": [[2, 0, "st. louis cardinals"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 3, "%st. louis cardinals%"]], "sel": 5}`
- Error: operator 3 is not executable

## test:14639:2-12208071-5

- Question: Who did the Blue Jays lose to on July 16?
- Gold: `{"sel": 3, "conds": [[0, 0, "july 16"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "July 16"]], "sel": 1}`
- Error: logical-form mismatch

## test:14646:2-1252069-1

- Question: How many laps did Duke Nelson complete when his qualifying time was 122.951?
- Gold: `{"sel": 5, "conds": [[2, 0, "122.951"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "122.951"]], "sel": 5}`
- Error: logical-form mismatch

## test:14647:2-1252069-1

- Question: How many laps did Duke Nelson complete when his qualifying time was 136.498?
- Gold: `{"sel": 5, "conds": [[2, 0, "136.498"]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "136.498"]], "sel": 5}`
- Error: logical-form mismatch

## test:14654:2-12635188-6

- Question: Name the attendance for atlanta braves opponent for september 9
- Gold: `{"sel": 4, "conds": [[1, 0, "atlanta braves"], [0, 0, "september 9"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "september 9"]], "sel": 4}`
- Error: logical-form mismatch

## test:14681:2-1233840-1

- Question: What year did Austria-Marlboro BRM get more than 0 points?
- Gold: `{"sel": 0, "conds": [[1, 0, "austria-marlboro brm"], [4, 1, 0]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Austria-Marlboro BRM"], [4, 1, 0]], "sel": 0}`
- Error: logical-form mismatch

## test:14690:2-1252120-1

- Question: How many laps were completed with a start of 33, and a finish of 18?
- Gold: `{"sel": 5, "conds": [[1, 0, "33"], [4, 0, "18"]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "33"], [4, 0, "18"]], "sel": 5}`
- Error: logical-form mismatch

## test:14738:2-12253523-2

- Question: What nation had more than 97 Gold Medals and fewer than 332 Silver Medals?
- Gold: `{"sel": 5, "conds": [[2, 1, 97], [3, 2, 332]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 1, 97], [3, 2, 332]], "sel": 1}`
- Error: logical-form mismatch

## test:14739:2-12253523-2

- Question: What nation had 135 Bronze medals?
- Gold: `{"sel": 4, "conds": [[5, 0, 135]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 0, 135]], "sel": 1}`
- Error: logical-form mismatch

## test:14740:2-12869529-1

- Question: What is the area of Ulim with less than 30 villages?
- Gold: `{"sel": 2, "conds": [[1, 0, "ulim"], [6, 2, 30]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Ulim"], [6, 2, 30]], "sel": 2}`
- Error: logical-form mismatch

## test:14747:2-12962773-7

- Question: What player was born in 1978 and smaller than 1.92?
- Gold: `{"sel": 4, "conds": [[1, 2, 1.92], [3, 1, 1978]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, 1978], [1, 2, 1.92]], "sel": 0}`
- Error: logical-form mismatch

## test:14763:2-1263207-1

- Question: Which season did the Minnesota Kicks lose 13 games and scored 156 points?
- Gold: `{"sel": 0, "conds": [[1, 0, 13], [2, 0, 156]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "13"], [2, 0, "156"]], "sel": 0}`
- Error: logical-form mismatch

## test:14764:2-1263207-1

- Question: Which season did the Kicks have more than 137 points with 13 losses and an average attendance larger than 23,121?
- Gold: `{"sel": 0, "conds": [[2, 1, 137], [4, 1, "23,121"], [1, 0, 13]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 1, 137], [1, 0, 13], [4, 1, 23121]], "sel": 0}`
- Error: logical-form mismatch

## test:14778:2-12206344-7

- Question: Who did the team lose to on September 8?
- Gold: `{"sel": 3, "conds": [[0, 0, "september 8"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "september 8"]], "sel": 1}`
- Error: logical-form mismatch

## test:14819:2-12710384-4

- Question: Which totals tournament has the lowest wins and top-25 less than 4?
- Gold: `{"sel": 1, "conds": [[0, 0, "totals"], [4, 2, 4]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[1, 0, 0], [4, 2, 4]], "sel": 0}`
- Error: logical-form mismatch

## test:14836:2-1249707-1

- Question: What's the transfer distance (km) larger than 36.5, at the station of guangximen?
- Gold: `{"sel": 5, "conds": [[4, 1, 36.5], [1, 0, "guangximen"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 1, 36.5], [1, 0, "guangximen"]], "sel": 4}`
- Error: logical-form mismatch

## test:14865:2-12194988-2

- Question: How many points has more than 15 wins and less than 10 losses?
- Gold: `{"sel": 3, "conds": [[4, 1, 15], [6, 2, 10]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 1, 15], [6, 2, 10]], "sel": 3}`
- Error: logical-form mismatch

## test:14919:2-13199257-2

- Question: What is the total number of 3rd place finishes for racers with 0 titles?
- Gold: `{"sel": 5, "conds": [[6, 2, 0]], "agg": 4}`
- Prediction: `{"agg": 4, "conds": [[6, 0, 0]], "sel": 5}`
- Error: logical-form mismatch

## test:14920:2-13199257-2

- Question: What is the sum of the number of wins for racers with 0 3rd place finishes?
- Gold: `{"sel": 3, "conds": [[5, 2, 0]], "agg": 4}`
- Prediction: `{"agg": 4, "conds": [[5, 0, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:14924:2-13042949-1

- Question: Name the total number of lost when goals scored is less than 22 and goals conceded is more than 27
- Gold: `{"sel": 4, "conds": [[5, 2, 22], [6, 1, 27]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[5, 2, 22], [6, 1, 27]], "sel": 4}`
- Error: logical-form mismatch

## test:14931:2-12741476-13

- Question: What round was matt roth drafted?
- Gold: `{"sel": 2, "conds": [[0, 0, "matt roth"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "matt roth"]], "sel": 2}`
- Error: logical-form mismatch

## test:14943:2-125458-1

- Question: Which non-violent crime rate per 1000 peope has the following criteria: crime rate per 1000 greater than 82.8, violent crime smaller than 305, robbery less than 147 and a crime index total greater than 1540?
- Gold: `{"sel": 5, "conds": [[4, 1, 82.8], [2, 2, 305], [9, 2, 147], [1, 1, 1540]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 1, 82.8], [2, 2, 305], [9, 2, 147], [1, 1, 1540]], "sel": 6}`
- Error: logical-form mismatch

## test:14946:2-12694743-1

- Question: What record had an alca-271 cd?
- Gold: `{"sel": 0, "conds": [[3, 0, "cd"], [4, 0, "alca-271"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "cd"], [4, 0, "alca-271"]], "sel": 2}`
- Error: logical-form mismatch

## test:14954:2-12271718-2

- Question: What is the largest frequency owned by multicultural broadcasting with a Format of vietnamese?
- Gold: `{"sel": 1, "conds": [[5, 0, "owned by multicultural broadcasting"], [3, 0, "vietnamese"]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[3, 0, "Vietnamese"], [5, 3, "Multicultural Broadcasting"]], "sel": 1}`
- Error: operator 3 is not executable

## test:14959:2-12874689-10

- Question: Who has the lowest FA cup and has a total over 46?
- Gold: `{"sel": 2, "conds": [[4, 1, 46]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[2, 0, 0], [4, 1, 46]], "sel": 0}`
- Error: logical-form mismatch

## test:14964:2-12796733-3

- Question: How many wins did he have when he made over 2 cuts and had under 2 top 10s?
- Gold: `{"sel": 1, "conds": [[4, 1, 2], [2, 2, 2]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[4, 1, 2], [2, 2, 2]], "sel": 1}`
- Error: logical-form mismatch

## test:14965:2-12206319-2

- Question: Who was the opponent of the game that 31,293 people attended that had a final score of 9 - 6.
- Gold: `{"sel": 1, "conds": [[2, 0, "9 - 6"], [4, 1, "31,293"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "9 - 6"], [4, 0, "31,293"]], "sel": 1}`
- Error: logical-form mismatch

## test:14967:2-12206319-2

- Question: How many people went to the game with the record of 8-10?
- Gold: `{"sel": 4, "conds": [[5, 0, "8-10"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[5, 0, "8-10"]], "sel": 4}`
- Error: logical-form mismatch

## test:14972:2-12481356-2

- Question: How many people were in attendance at week 16?
- Gold: `{"sel": 4, "conds": [[0, 0, 16]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[0, 0, 16]], "sel": 4}`
- Error: logical-form mismatch

## test:15007:2-1296513-13

- Question: Which event had a prize of $2,434,061?
- Gold: `{"sel": 3, "conds": [[4, 0, "$2,434,061"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "$2,434,061"]], "sel": 1}`
- Error: logical-form mismatch

## test:15026:2-1284906-3

- Question: What is the highest position less than 7 that had more than 421,760 in sales for the song Don't Stop Movin'?
- Gold: `{"sel": 3, "conds": [[4, 1, "421,760"], [1, 0, "don't stop movin'"], [0, 2, 7]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[3, 2, 7], [4, 1, "421,760"], [1, 0, "don't stop movin'"]], "sel": 3}`
- Error: logical-form mismatch

## test:15027:2-1284906-3

- Question: What position is the song Have You Ever with more than 1,037,235 in sales?
- Gold: `{"sel": 0, "conds": [[4, 1, "1,037,235"], [1, 0, "have you ever"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Have You Ever"], [4, 1, 1037235]], "sel": 0}`
- Error: logical-form mismatch

## test:15028:2-1284906-3

- Question: What were the total number of sales for the song 21 Seconds?
- Gold: `{"sel": 4, "conds": [[1, 0, "21 seconds"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "21 Seconds"]], "sel": 4}`
- Error: logical-form mismatch

## test:15048:2-12742744-1

- Question: Who has a transfer fee larger than 12 from ajax in 2006 while ranked higher than 17?
- Gold: `{"sel": 1, "conds": [[3, 1, 12], [0, 1, 17], [4, 1, 2006], [2, 0, "ajax"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[3, 1, "12"], [2, 0, "ajax"], [4, 0, "2006"], [0, 1, "17"]], "sel": 1}`
- Error: logical-form mismatch

## test:15051:2-12969596-1

- Question: Which film originated in France?
- Gold: `{"sel": 3, "conds": [[0, 0, "france"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "France"]], "sel": 1}`
- Error: logical-form mismatch

## test:15066:2-1235976-1

- Question: What is the number of points for the Entrant of escuderia bandeirantes earlier than 1952?
- Gold: `{"sel": 4, "conds": [[1, 0, "escuderia bandeirantes"], [0, 2, 1952]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "escuderia bandeirantes"], [0, 2, 1952]], "sel": 4}`
- Error: logical-form mismatch

## test:15070:2-12241356-2

- Question: What is the number for the Moroccan population when the name is Sebt Saiss and the 2004 population is more than 11212?
- Gold: `{"sel": 6, "conds": [[0, 0, "sebt saiss"], [4, 1, 11212]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Sebt Saiss"], [4, 1, 11212]], "sel": 6}`
- Error: logical-form mismatch

## test:15072:2-1252109-3

- Question: What is the highest year that has no more than 0 points?
- Gold: `{"sel": 0, "conds": [[4, 2, 0]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[4, 3, 0]], "sel": 0}`
- Error: operator 3 is not executable

## test:15074:2-1252109-3

- Question: What was the latest year that a Bardahl entrant had a Kurtis Kraft 500c chassis with no more than 0 points?
- Gold: `{"sel": 0, "conds": [[2, 0, "kurtis kraft 500c"], [1, 0, "bardahl"], [4, 2, 0]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[1, 0, "Bardahl"], [2, 0, "Kurtis Kraft 500C"], [4, 3, 0]], "sel": 0}`
- Error: operator 3 is not executable

## test:15082:2-12200520-3

- Question: What movie won with a date of 12/11/03
- Gold: `{"sel": 4, "conds": [[5, 0, "12/11/03"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "12/11/03"]], "sel": 0}`
- Error: logical-form mismatch

## test:15090:2-12733279-2

- Question: What was the pick number of Conor Jackson?
- Gold: `{"sel": 0, "conds": [[1, 0, "conor jackson"]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "conor jackson"]], "sel": 0}`
- Error: logical-form mismatch

## test:15105:2-1235356-2

- Question: What is the year when Spirit Tom's Racing had more than 3 points?
- Gold: `{"sel": 0, "conds": [[1, 0, "spirit tom's racing"], [4, 1, 3]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Spirit TOM's Racing"], [4, 1, 3]], "sel": 0}`
- Error: logical-form mismatch

## test:15106:2-12536613-1

- Question: Name the average week for attendance of 75,111
- Gold: `{"sel": 0, "conds": [[4, 0, "75,111"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 0, 75111]], "sel": 0}`
- Error: logical-form mismatch

## test:15108:2-12562232-1

- Question: Who had the smallest points in 3rd place but had a position greater than 8?
- Gold: `{"sel": 3, "conds": [[4, 0, "3rd"], [0, 1, 8]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[0, 1, 8], [4, 0, "3rd"]], "sel": 1}`
- Error: logical-form mismatch

## test:15111:2-12617978-13

- Question: how much money was requested on the show which aired on 4 september 2011?
- Gold: `{"sel": 4, "conds": [[1, 0, "4 september 2011"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "4 september 2011"]], "sel": 4}`
- Error: logical-form mismatch

## test:15132:2-1262579-2

- Question: Which chassis was used when over 6 points were earned?
- Gold: `{"sel": 1, "conds": [[4, 0, 6]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 1, 6]], "sel": 1}`
- Error: logical-form mismatch

## test:15139:2-12556269-1

- Question: What is the lowest number of bronze medals for a country with less than 1 gold and 0 silver?
- Gold: `{"sel": 3, "conds": [[1, 0, 1], [2, 2, 0]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[1, 2, 1], [2, 0, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:15140:2-12164513-1

- Question: What was the score of the game for April 16?
- Gold: `{"sel": 3, "conds": [[0, 0, "april 16"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "april 16"]], "sel": 2}`
- Error: logical-form mismatch

## test:15152:2-13065827-1

- Question: With a Division II of Portsmouth, what is the Division IV?
- Gold: `{"sel": 4, "conds": [[3, 0, "portsmouth"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Portsmouth"]], "sel": 4}`
- Error: logical-form mismatch

## test:15155:2-1228324-1

- Question: What is total amount of points of entrants with a ford cosworth engine and a year later than 1991?
- Gold: `{"sel": 4, "conds": [[3, 0, "ford cosworth"], [0, 1, 1991]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[3, 0, "ford cosworth"], [0, 1, 1991]], "sel": 4}`
- Error: logical-form mismatch

## test:15161:2-1226579-1

- Question: Name the total number of points for beta team march 1975 and chassis of march 751
- Gold: `{"sel": 4, "conds": [[1, 0, "beta team march"], [0, 0, 1975], [2, 0, "march 751"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[1, 0, "beta team march"], [0, 0, 1975], [2, 0, "march 751"]], "sel": 4}`
- Error: logical-form mismatch

## test:15180:2-12453414-8

- Question: How many saves did the player with a 92.3% save rate and 217 goals have?
- Gold: `{"sel": 3, "conds": [[4, 0, "92.3%"], [2, 1, 217]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, 217], [4, 0, "92.3%"]], "sel": 3}`
- Error: logical-form mismatch

## test:15187:2-1218389-2

- Question: How many laps were driven by the racer who earned 4th place in 2013?
- Gold: `{"sel": 4, "conds": [[5, 0, "4th"], [0, 1, 2013]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 2013], [5, 0, "4th"]], "sel": 4}`
- Error: logical-form mismatch

## test:15191:2-13135264-11

- Question: Which Attendance  has a Game score less than 3, and a Score of 2 – 5?
- Gold: `{"sel": 6, "conds": [[0, 2, 3], [3, 0, "2 – 5"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 2, 3], [3, 0, "2 – 5"]], "sel": 6}`
- Error: logical-form mismatch

## test:15192:2-13135264-11

- Question: Who has Series of 2 – 3?
- Gold: `{"sel": 2, "conds": [[7, 0, "2 – 3"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[7, 0, "2 – 3"]], "sel": 4}`
- Error: logical-form mismatch

## test:15193:2-13135264-11

- Question: Who has  a Home of detroit on  april 22?
- Gold: `{"sel": 2, "conds": [[4, 0, "detroit"], [1, 0, "april 22"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "detroit"], [1, 0, "april 22"]], "sel": 5}`
- Error: logical-form mismatch

## test:15218:2-12937449-3

- Question: What were the number of sales before 1991?
- Gold: `{"sel": 3, "conds": [[0, 2, 1991]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 2, 1991]], "sel": 3}`
- Error: logical-form mismatch

## test:15220:2-12538628-1

- Question: What year was the (Barcaldine) larger than 1,868 and the (Aramac) lower than 1,592?
- Gold: `{"sel": 0, "conds": [[2, 1, "1,868"], [3, 2, "1,592"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[2, 1, 1868], [3, 2, 1592]], "sel": 0}`
- Error: logical-form mismatch

## test:15222:2-12538628-1

- Question: What year had a Poulation (Total) of 3,492 and a (Barcaldine) less than 1,818?
- Gold: `{"sel": 0, "conds": [[1, 0, "3,492"], [2, 2, "1,818"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "3,492"], [2, 2, "1,818"]], "sel": 0}`
- Error: logical-form mismatch

## test:15225:2-12538628-1

- Question: What Year has an (Aramac) of 832 and a Population (Total) less than 3,762?
- Gold: `{"sel": 0, "conds": [[3, 0, 832], [1, 2, "3,762"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "832"], [1, 2, "3,762"]], "sel": 0}`
- Error: logical-form mismatch

## test:15233:2-12378197-1

- Question: Who is retired with eyes of dark brown, and black hair?
- Gold: `{"sel": 4, "conds": [[2, 0, "dark brown"], [1, 0, "black"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "black"], [2, 0, "dark brown"], [4, 0, "yes"]], "sel": 0}`
- Error: logical-form mismatch

## test:15243:2-1234983-2

- Question: In 1985, how many points were earned by the entrant with the March 85B chassis?
- Gold: `{"sel": 4, "conds": [[0, 0, 1985], [2, 0, "march 85b"]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[0, 0, 1985], [2, 0, "march 85b"]], "sel": 4}`
- Error: logical-form mismatch

## test:15244:2-1234983-2

- Question: How many points did Corbari Italia earn in 1985?
- Gold: `{"sel": 4, "conds": [[1, 0, "corbari italia"], [0, 0, 1985]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 0, 1985], [1, 0, "Corbari Italia"]], "sel": 4}`
- Error: logical-form mismatch

## test:15264:2-12553636-3

- Question: In what heat did the swimmer in Lane 6 rank higher than 7 with a time of 4:08.27?
- Gold: `{"sel": 1, "conds": [[2, 0, 6], [4, 0, "4:08.27"], [0, 1, 7]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, 6], [0, 0, 7], [4, 0, "4:08.27"]], "sel": 1}`
- Error: logical-form mismatch

## test:15289:2-1219767-1

- Question: What is the total points of teams using a ligier js11/15 chassis?
- Gold: `{"sel": 4, "conds": [[2, 0, "ligier js11/15"]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[2, 0, "ligier js11/15"]], "sel": 4}`
- Error: logical-form mismatch

## test:15294:2-12807904-2

- Question: How many tries against were there with 17 losses?
- Gold: `{"sel": 7, "conds": [[3, 0, "17"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "17"]], "sel": 7}`
- Error: logical-form mismatch

## test:15295:2-12807904-2

- Question: How many losses were there with 103 tries for?
- Gold: `{"sel": 3, "conds": [[6, 0, "103"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[6, 0, "103"]], "sel": 3}`
- Error: logical-form mismatch

## test:15301:2-1278594-2

- Question: What is the rank of the town with a population of 258?
- Gold: `{"sel": 0, "conds": [[1, 0, 258]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, 258]], "sel": 0}`
- Error: logical-form mismatch

## test:15302:2-12562153-2

- Question: In what Year is the Isis Population 4,082 and the Regional Population less than 55,990?
- Gold: `{"sel": 0, "conds": [[5, 0, "4,082"], [1, 2, "55,990"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "4,082"], [1, 2, "55,990"]], "sel": 0}`
- Error: logical-form mismatch

## test:15321:2-12531523-4

- Question: where did arron oberholser play?
- Gold: `{"sel": 2, "conds": [[1, 0, "arron oberholser"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "arron oberholser"]], "sel": 0}`
- Error: logical-form mismatch

## test:15324:2-13107350-1

- Question: When was the earliest first game with 11 played and 12 games lost?
- Gold: `{"sel": 0, "conds": [[1, 1, 11], [3, 0, 12]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[1, 0, 11], [3, 0, 12]], "sel": 0}`
- Error: logical-form mismatch

## test:15326:2-13107350-1

- Question: How many first games are associated with 5 games played and under 3 games lost?
- Gold: `{"sel": 0, "conds": [[1, 0, 5], [3, 2, 3]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[1, 0, 5], [3, 2, 3]], "sel": 0}`
- Error: logical-form mismatch

## test:15328:2-13089967-1

- Question: How many times was there a draw when played is more than 4 and the first game is in 2000?
- Gold: `{"sel": 2, "conds": [[1, 1, 4], [0, 0, 2000]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 1, 4], [0, 0, 2000]], "sel": 2}`
- Error: logical-form mismatch

## test:15329:2-13089967-1

- Question: what is the most games lost when there were 0 draws?
- Gold: `{"sel": 3, "conds": [[2, 2, 0]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[2, 0, 0]], "sel": 3}`
- Error: logical-form mismatch

## test:15332:2-13089967-1

- Question: how many draws are there when percentage is 100.00% and played is 7?
- Gold: `{"sel": 2, "conds": [[4, 0, "100.00%"], [1, 0, 7]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "100.00%"], [1, 0, 7]], "sel": 2}`
- Error: logical-form mismatch

## test:15344:2-12886178-5

- Question: How many games played when the points for is 369?
- Gold: `{"sel": 1, "conds": [[4, 0, "369"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "369"]], "sel": 1}`
- Error: logical-form mismatch

## test:15354:2-1252070-1

- Question: How many laps were in 1958?
- Gold: `{"sel": 5, "conds": [[0, 0, "1958"]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[0, 0, "1958"]], "sel": 5}`
- Error: logical-form mismatch

## test:15365:2-1304940-1

- Question: How many votes did Other receive where Bush received less than 154,204 votes, and Kerry received 41.7% and more than 98,066 votes?
- Gold: `{"sel": 6, "conds": [[4, 2, "154,204"], [1, 0, "41.7%"], [2, 1, "98,066"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[4, 2, "154,204"], [1, 0, "41.7%"], [2, 1, "98,066"]], "sel": 6}`
- Error: logical-form mismatch

## test:15367:2-1304940-1

- Question: How many votes did Others receive where Kerry has 44.6%, and Bush more than 163,650 votes?
- Gold: `{"sel": 6, "conds": [[1, 0, "44.6%"], [4, 1, "163,650"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "44.6%"], [4, 1, 163650]], "sel": 6}`
- Error: logical-form mismatch

## test:15373:2-1257169-11

- Question: What is the total for danny allsopp?
- Gold: `{"sel": 4, "conds": [[0, 0, "danny allsopp"]], "agg": 0}`
- Prediction: `{"agg": 4, "conds": [[0, 0, "danny allsopp"]], "sel": 4}`
- Error: logical-form mismatch

## test:15379:2-1235871-1

- Question: How many points did the Cosworth v8 engine get in 1972?
- Gold: `{"sel": 4, "conds": [[0, 0, 1972], [3, 0, "cosworth v8"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "cosworth v8"], [0, 0, 1972]], "sel": 4}`
- Error: logical-form mismatch

## test:15393:2-12167166-2

- Question: What is the score of Goal For which has a Ties larger 0?
- Gold: `{"sel": 5, "conds": [[4, 1, 0]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[4, 1, 0]], "sel": 5}`
- Error: logical-form mismatch

## test:15396:2-1314472-1

- Question: Name the D46 when it has D 44 of ← majority
- Gold: `{"sel": 2, "conds": [[4, 0, "← majority"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "\u001a majority"]], "sel": 2}`
- Error: logical-form mismatch

## test:15409:2-13014350-1

- Question: How many goals were scored when they had over 28 points and played over 18 games?
- Gold: `{"sel": 5, "conds": [[7, 1, 28], [2, 1, 18]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[7, 1, 28], [2, 1, 18]], "sel": 5}`
- Error: logical-form mismatch

## test:15410:2-13014350-1

- Question: What place is associated with under 28 points, under 11 games lost, and under 18 games played?
- Gold: `{"sel": 0, "conds": [[7, 2, 28], [4, 2, 11], [2, 2, 18]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[7, 2, 28], [4, 2, 11], [2, 2, 18]], "sel": 0}`
- Error: logical-form mismatch

## test:15411:2-13014350-1

- Question: How many points are there when they have under 27 goals scored, conceded 24 goals, and lost less than 6 times?
- Gold: `{"sel": 7, "conds": [[5, 2, 27], [6, 0, 24], [4, 2, 6]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[5, 2, 27], [6, 0, 24], [4, 2, 6]], "sel": 7}`
- Error: logical-form mismatch

## test:15419:2-12109851-5

- Question: How many losses altogether were had by teams that won 12 times, had 40-4 points, and more than 57 goals?
- Gold: `{"sel": 6, "conds": [[4, 0, 12], [3, 0, "40-4"], [7, 1, 57]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[4, 0, 12], [3, 0, "40-4"], [7, 1, 57]], "sel": 6}`
- Error: logical-form mismatch

## test:15424:2-13327331-1

- Question: What is the number of games played in the season before 2005?
- Gold: `{"sel": 1, "conds": [[0, 2, 2005]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[0, 2, 2005]], "sel": 1}`
- Error: logical-form mismatch

## test:15428:2-13166646-1

- Question: How much money has 76-70-68-73=287 as a score?
- Gold: `{"sel": 5, "conds": [[3, 0, "76-70-68-73=287"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "76-70-68-73=287"]], "sel": 5}`
- Error: logical-form mismatch

## test:15435:2-1251878-1

- Question: What camera has the highest Mpix with an aspect ratio of 2:1, a height less than 1536, and a width smaller than 2048?
- Gold: `{"sel": 3, "conds": [[4, 0, "2:1"], [2, 2, 1536], [1, 2, 2048]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "2:1"], [2, 2, 1536], [1, 2, 2048]], "sel": 0}`
- Error: logical-form mismatch

## test:15436:2-1251878-1

- Question: What is the max fps of a camera with mpix larger than 8.4 and frame size of 4k 16:9?
- Gold: `{"sel": 5, "conds": [[3, 1, 8.4], [0, 0, "4k 16:9"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 1, 8.4], [0, 0, "4K 16:9"]], "sel": 5}`
- Error: logical-form mismatch

## test:15450:2-12555835-1

- Question: In what year was the Population of Eacham 6,074 and the population of Atherton was less than 10,119?
- Gold: `{"sel": 0, "conds": [[5, 0, "6,074"], [3, 2, "10,119"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "6,074"], [3, 2, "10,119"]], "sel": 0}`
- Error: logical-form mismatch

## test:15451:2-12555835-1

- Question: What was the population of Herberton when Mareeba had 17,129 people and Eacham had a population smaller than 5,609?
- Gold: `{"sel": 4, "conds": [[2, 0, "17,129"], [5, 2, "5,609"]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "17,129"], [5, 2, "5,609"]], "sel": 4}`
- Error: logical-form mismatch

## test:15507:2-1235386-1

- Question: What year did the Cosworth v8 engine participate in?
- Gold: `{"sel": 0, "conds": [[3, 0, "cosworth v8"]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "cosworth v8"]], "sel": 0}`
- Error: logical-form mismatch

## test:15508:2-1235386-1

- Question: Which year did the team receive more than 0 points?
- Gold: `{"sel": 0, "conds": [[4, 1, 0]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[4, 1, 0]], "sel": 0}`
- Error: logical-form mismatch

## test:15522:2-12898083-1

- Question: What is the highest number of bronzes for countries ranking over 5 with 0 golds?
- Gold: `{"sel": 4, "conds": [[0, 1, 5], [2, 2, 0]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[0, 1, 5], [2, 0, 0]], "sel": 4}`
- Error: logical-form mismatch

## test:15529:2-12886178-6

- Question: How many matches played are associated with 20 losses?
- Gold: `{"sel": 1, "conds": [[3, 0, "20"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, "20"]], "sel": 1}`
- Error: logical-form mismatch

## test:15540:2-12919633-1

- Question: Name the film title that was norwegian
- Gold: `{"sel": 1, "conds": [[2, 0, "norwegian"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "norwegian"]], "sel": 1}`
- Error: logical-form mismatch

## test:15563:2-12207474-9

- Question: What game did they lose by 6 - 5?
- Gold: `{"sel": 3, "conds": [[2, 0, "6 - 5"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "6 - 5"]], "sel": 0}`
- Error: logical-form mismatch

## test:15569:2-13038386-1

- Question: How many golds for west germany with over 8 total?
- Gold: `{"sel": 2, "conds": [[1, 0, "west germany"], [5, 1, 8]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[5, 1, 8], [1, 0, "west germany"]], "sel": 2}`
- Error: logical-form mismatch

## test:15570:2-13038386-1

- Question: How many golds for nations with under 1 bronze?
- Gold: `{"sel": 2, "conds": [[4, 2, 1]], "agg": 4}`
- Prediction: `{"agg": 3, "conds": [[4, 2, 1]], "sel": 2}`
- Error: logical-form mismatch

## test:15571:2-13038386-1

- Question: How many total medals for the nation ranked 7 with 1 silver and under 4 bronzes?
- Gold: `{"sel": 5, "conds": [[4, 2, 4], [3, 0, 1], [0, 0, "7"]], "agg": 5}`
- Prediction: `{"agg": 3, "conds": [[0, 0, 7], [3, 0, 1], [4, 2, 4]], "sel": 5}`
- Error: logical-form mismatch

## test:15603:2-12821159-11

- Question: What is the total amount of Top-25 having a Top-5 greater than 1?
- Gold: `{"sel": 4, "conds": [[2, 1, 1]], "agg": 3}`
- Prediction: `{"agg": 4, "conds": [[2, 1, 1]], "sel": 4}`
- Error: logical-form mismatch

## test:15625:2-12807904-5

- Question: How many losses were there with 208 points?
- Gold: `{"sel": 3, "conds": [[4, 0, "208"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 0, "208"]], "sel": 3}`
- Error: logical-form mismatch

## test:15627:2-1226549-4

- Question: What car has a March 90ca Chassis?
- Gold: `{"sel": 2, "conds": [[1, 0, "march 90ca"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "march 90ca"]], "sel": 5}`
- Error: logical-form mismatch

## test:15631:2-1251765-20

- Question: What is the corresponding 1930s for 2000 and 1940?
- Gold: `{"sel": 2, "conds": [[9, 0, 2000], [3, 2, 1940]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[9, 0, 2000], [3, 0, 1940]], "sel": 2}`
- Error: logical-form mismatch

## test:15633:2-1251765-20

- Question: What is the range for the 1980s that correspond to a grid 1910s of 1912, and a 1940s before 1942
- Gold: `{"sel": 7, "conds": [[0, 0, 1912], [3, 2, 1942]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "1912"], [3, 2, "1942"]], "sel": 7}`
- Error: logical-form mismatch

## test:15634:2-1251765-20

- Question: what is the lowest year in the 1910s that would be in the row were the 1950s are no larger than 1952, and the 1980s are no smaller than 1981?
- Gold: `{"sel": 0, "conds": [[4, 2, 1952], [7, 1, 1981]], "agg": 2}`
- Prediction: `{"agg": 2, "conds": [[4, 2, 1952], [7, 3, 1981]], "sel": 0}`
- Error: operator 3 is not executable

## test:15641:2-1236194-1

- Question: What is the number of finish of the Qual of 159.384?
- Gold: `{"sel": 4, "conds": [[2, 0, "159.384"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[2, 0, "159.384"]], "sel": 4}`
- Error: logical-form mismatch

## test:15645:2-12207755-4

- Question: Who did they lose to on May 20?
- Gold: `{"sel": 3, "conds": [[0, 0, "may 20"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "may 20"]], "sel": 1}`
- Error: logical-form mismatch

## test:15669:2-12837881-2

- Question: How many broadband subscribers are there where the population is ~3,644,070?
- Gold: `{"sel": 3, "conds": [[5, 0, "~3,644,070"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[5, 0, "~3,644,070"]], "sel": 3}`
- Error: logical-form mismatch

## test:15671:2-12837881-2

- Question: How many broadband subscribers are there where there are ~47,372 users?
- Gold: `{"sel": 3, "conds": [[1, 0, "~47,372"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "~47,372"]], "sel": 3}`
- Error: logical-form mismatch

## test:15718:2-1226507-1

- Question: What chassis did team lotus use after 1964?
- Gold: `{"sel": 2, "conds": [[1, 0, "team lotus"], [0, 1, 1964]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 1, 1964]], "sel": 2}`
- Error: logical-form mismatch

## test:15730:2-1255353-1

- Question: What category did MCG get a nominee in?
- Gold: `{"sel": 1, "conds": [[4, 0, "mcg"], [5, 0, "nominee"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "MCG"]], "sel": 1}`
- Error: logical-form mismatch

## test:15737:2-12821570-2

- Question: What was the highest number of points scored when there was a draw of 2 and when the amount played was 18?
- Gold: `{"sel": 7, "conds": [[3, 0, 2], [2, 2, 18]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[3, 0, 2], [2, 0, 18]], "sel": 7}`
- Error: logical-form mismatch

## test:15750:2-12530926-8

- Question: What is the 2004 tournament that has a Q1 of 2011?
- Gold: `{"sel": 8, "conds": [[12, 0, "q1"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[12, 0, "Q1"]], "sel": 0}`
- Error: logical-form mismatch

## test:15787:2-12755786-8

- Question: What is the Challenge Cup total with a League of 1, Player Simon Storey, and a Total greater than 1?
- Gold: `{"sel": 4, "conds": [[1, 0, 1], [0, 0, "simon storey"], [5, 1, 1]], "agg": 4}`
- Prediction: `{"agg": 0, "conds": [[1, 0, 1], [0, 0, "Simon Storey"], [5, 1, 1]], "sel": 4}`
- Error: logical-form mismatch

## test:15800:2-12109851-4

- Question: Name the most wins which have clubbed of elche cf and goals against more than 43
- Gold: `{"sel": 4, "conds": [[1, 0, "elche cf"], [8, 1, 43]], "agg": 1}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "Elche CF"], [8, 1, 43]], "sel": 4}`
- Error: logical-form mismatch

## test:15802:2-13312864-1

- Question: Shirt number of 18, and a Height larger than 195 has how much weight?
- Gold: `{"sel": 3, "conds": [[0, 0, 18], [4, 1, 195]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, 18], [4, 1, 195]], "sel": 3}`
- Error: logical-form mismatch

## test:15834:2-12441518-1

- Question: How many episodes were portrayed by Nick Jonas?
- Gold: `{"sel": 4, "conds": [[1, 0, "nick jonas"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Nick Jonas"]], "sel": 4}`
- Error: logical-form mismatch

## test:15862:2-1232836-4

- Question: Who has the highest ranking from  1996–13, and more than 17 goals?
- Gold: `{"sel": 0, "conds": [[3, 0, "1996–13"], [4, 1, 17]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "1996–13"], [4, 1, 17]], "sel": 2}`
- Error: logical-form mismatch

## test:15866:2-1232836-4

- Question: Who had fewer goals than 4 during the years of 1996–13?
- Gold: `{"sel": 4, "conds": [[0, 2, 4], [3, 0, "1996–13"]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "1996–13"], [4, 2, 4]], "sel": 2}`
- Error: logical-form mismatch

## test:15868:2-12962193-3

- Question: what is the top-5 when the tournament is totals and the top-25 is more than 4?
- Gold: `{"sel": 2, "conds": [[0, 0, "totals"], [3, 1, 4]], "agg": 5}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Totals"], [3, 1, 4]], "sel": 2}`
- Error: logical-form mismatch

## test:15870:2-12962193-3

- Question: what is the highest top-5 when the top-25 is less than 4, cuts made is more than 3 and wins is 0?
- Gold: `{"sel": 2, "conds": [[3, 2, 4], [5, 1, 3], [1, 2, 0]], "agg": 1}`
- Prediction: `{"agg": 1, "conds": [[3, 2, 4], [5, 1, 3], [1, 0, 0]], "sel": 2}`
- Error: logical-form mismatch

## test:15873:2-1226335-1

- Question: After 1972, how many points did Marlboro Team Alfa Romeo have?
- Gold: `{"sel": 4, "conds": [[0, 1, 1972], [1, 0, "marlboro team alfa romeo"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[0, 1, 1972], [1, 0, "marlboro team alfa romeo"]], "sel": 4}`
- Error: logical-form mismatch
