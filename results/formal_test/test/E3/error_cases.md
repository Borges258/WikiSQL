# Error cases

## test:5:1-10083598-1

- Question: What was the number of race that Kevin Curtain won?
- Gold: `{"sel": 0, "conds": [[4, 0, "Kevin Curtain"]], "agg": 3}`
- Prediction: `{"agg": 3, "conds": [[6, 0, "Kevin Curtain"]], "sel": 6}`
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

## test:239:1-11456251-5

- Question: What is the number of generators where the power capicity is 78.7?
- Gold: `{"sel": 1, "conds": [[2, 0, "78.7"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "78.7"]], "sel": 1}`
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

## test:269:1-11630008-4

- Question: What is the first season written by joseph hampton & dani renee?
- Gold: `{"sel": 1, "conds": [[4, 0, "Joseph Hampton & Dani Renee"]], "agg": 2}`
- Prediction: `{"agg": 0, "conds": [[4, 0, "Joseph Hampton & Dani Renee"]], "sel": 1}`
- Error: logical-form mismatch

## test:272:1-11630008-4

- Question: What is the series number for the title "Bad Influence"
- Gold: `{"sel": 0, "conds": [[2, 0, "\"Bad Influence\""]], "agg": 1}`
- Prediction: `{"agg": 0, "conds": [[2, 0, "Bad Influence"]], "sel": 0}`
- Error: logical-form mismatch

## test:283:1-1166259-1

- Question: How many points are there when the lost is 26?
- Gold: `{"sel": 5, "conds": [[3, 0, 26]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[3, 0, 26]], "sel": 5}`
- Error: logical-form mismatch

## test:288:1-11674683-2

- Question: Name the number of swimsuit for israel
- Gold: `{"sel": 2, "conds": [[0, 0, "Israel"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Israel"]], "sel": 2}`
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
- Prediction: `{"agg": 4, "conds": [[0, 0, "human capital"]], "sel": 3}`
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
- Prediction: `{"agg": 0, "conds": [[4, 0, "5 (100)"], [1, 0, "Plywood"]], "sel": 0}`
- Error: logical-form mismatch

## test:430:1-12094300-1

- Question: What is the average score when the swimsuit score is 8.503?
- Gold: `{"sel": 5, "conds": [[3, 0, "8.503"]], "agg": 0}`
- Prediction: `{"agg": 5, "conds": [[3, 0, "8.503"]], "sel": 5}`
- Error: logical-form mismatch

## test:438:1-12165135-1

- Question: What is the pick number of the defensive back?
- Gold: `{"sel": 0, "conds": [[3, 0, "Defensive Back"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[3, 0, "defensive back"]], "sel": 0}`
- Error: logical-form mismatch

## test:452:1-12175755-1

- Question: What theme placed as #3 in the finale?
- Gold: `{"sel": 5, "conds": [[1, 0, "Finale"], [4, 0, "3"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Top 2"], [4, 0, "3"]], "sel": 1}`
- Error: logical-form mismatch

## test:456:1-12175755-1

- Question: What is the song choice when the theme is not aired?
- Gold: `{"sel": 1, "conds": [[2, 0, "Not Aired"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[1, 0, "Not Aired"]], "sel": 2}`
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
- Prediction: `{"agg": 3, "conds": [[2, 0, "the great mayoralty campaign"]], "sel": 0}`
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

## test:564:1-12828723-4

- Question: How many tries for are for 473 points for?
- Gold: `{"sel": 7, "conds": [[5, 0, "473"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "473"]], "sel": 7}`
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

## test:620:1-1305623-12

- Question: How many gold medals does each school who has a total of 1 medal have?
- Gold: `{"sel": 1, "conds": [[4, 0, 1]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[4, 0, 1]], "sel": 1}`
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

## test:780:1-1342379-5

- Question: Who was the incumbent when henry e. barbour ran?
- Gold: `{"sel": 5, "conds": [[1, 0, "Henry E. Barbour"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[5, 0, "Henry E. Barbour (R) Unopposed"]], "sel": 1}`
- Error: logical-form mismatch

## test:789:1-1342393-42

- Question: What was the total number of votes for Tom Connally
- Gold: `{"sel": 3, "conds": [[1, 0, "Tom Connally"]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[1, 0, "Tom Connally"]], "sel": 5}`
- Error: logical-form mismatch

## test:807:1-13464416-6

- Question: how many times was the participation at omni coliseum 7,194?
- Gold: `{"sel": 0, "conds": [[7, 0, "Omni Coliseum 7,194"]], "agg": 0}`
- Prediction: `{"agg": 3, "conds": [[7, 0, "Omni Coliseum 7,194"]], "sel": 0}`
- Error: logical-form mismatch

## test:808:1-1354805-3

- Question: The minimum average number of dancers is 34.1 how many times
- Gold: `{"sel": 4, "conds": [[5, 0, "34.1"]], "agg": 2}`
- Prediction: `{"agg": 3, "conds": [[5, 0, "34.1"]], "sel": 4}`
- Error: logical-form mismatch

## test:821:1-1359212-2

- Question: where is hte second place winner from united kingdom?
- Gold: `{"sel": 1, "conds": [[7, 0, "United Kingdom"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[7, 0, "United Kingdom"]], "sel": 10}`
- Error: logical-form mismatch

## test:824:1-1359212-2

- Question: what amount has spain as second place and the language is russian?
- Gold: `{"sel": 6, "conds": [[7, 0, "Spain"], [2, 0, "Russian"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[7, 0, "spain"], [2, 0, "russian"]], "sel": 5}`
- Error: logical-form mismatch

## test:825:1-13605170-2

- Question: how many Curtiss XBTC aircraft are retired?
- Gold: `{"sel": 4, "conds": [[0, 0, "Curtiss XBTC"]], "agg": 3}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "Curtiss XBTC"]], "sel": 4}`
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

## test:908:1-14035132-3

- Question: On what date did the episode with a series number 31, with a story written by William Reiss, air for the first time? 
- Gold: `{"sel": 6, "conds": [[5, 0, "William Reiss"], [0, 0, "31"]], "agg": 0}`
- Prediction: `{"agg": 0, "conds": [[0, 0, "31"], [4, 0, "William Reiss"]], "sel": 6}`
- Error: logical-form mismatch

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
