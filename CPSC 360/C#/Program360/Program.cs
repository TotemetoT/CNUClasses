using System;

namespace Program360
{
    public class Soccer
    {
        public static string[] getRankings(string[] matches)
        {
            string groupName = matches[0];
            List<string> foo =  new List<string>(matches); 
            foo.Remove(groupName);
            matches = foo.ToArray();
            Dictionary<string, int[]> teamScores = new Dictionary<string, int[]>();
            //Team:[points, games, wins, ties, losses, goal diff., goals scored, scored against]
            foreach (string m in matches)
            {
                string[] curr = Breakdown(m);
                int s1 = int.Parse(curr[1]);
                int s2 = int.Parse(curr[2]);
                //First Team
                if (!teamScores.ContainsKey(curr[0]))
                {
                    teamScores[curr[0]] = new int[8];
                }
                int[] t1 = teamScores[curr[0]];
                t1[1]++;
                //Win-Tie-Loss
                if (s1 > s2)
                {
                    t1[2]++;
                    t1[0] += 3;
                } 
                else if (s1 == s2)
                {
                    t1[3]++;
                    t1[0] += 1;
                }
                else
                {
                    t1[4]++;
                }
                
                t1[5] += s1 - s2;
                t1[6] += s1;
                t1[7] += s2;
                
                //Second Team
                if (!teamScores.ContainsKey(curr[3]))
                {
                    teamScores[curr[3]] = new int[8];
                }
                int[] t2 = teamScores[curr[3]];
                t2[1]++;
                //Win-Tie-Loss
                if (s2 > s1)
                {
                    t2[2]++;
                    t2[0] += 3;
                } 
                else if (s1 == s2)
                {
                    t2[3]++;
                    t2[0] += 1;
                }
                else
                {
                    t2[4]++;
                }
                
                t2[5] += s2 - s1;
                t2[6] += s2;
                t2[7] += s1;
            }

            String[] finalInfo = new String[teamScores.Count + 1];
            List<String> tempList = new List<string>();
            foreach (string team in teamScores.Keys) 
            {
                tempList.Add(team);
            }
            finalInfo[0] = groupName;
            int count = 1;
            while (tempList.Count > 0)
            {
                string sup = "";
                foreach (string team in tempList)
                {
                    string curr = team;
                    
                    if (sup == "")
                    {
                        sup = curr;
                    }
                    //Points
                    else if (teamScores[sup][0] == teamScores[curr][0])
                    {
                        //Wins
                        if (teamScores[sup][2] == teamScores[curr][2])
                        {
                            //Goal Difference
                            if (teamScores[sup][5] == teamScores[curr][5])
                            {
                                //Goals Scored
                                if (teamScores[sup][6] == teamScores[curr][6])
                                {
                                    //Less Matches Played
                                    if (teamScores[sup][1] == teamScores[curr][1])
                                    {
                                        if (string.Compare(curr, sup, StringComparison.OrdinalIgnoreCase) < 0)
                                        {
                                            sup = curr;
                                        }
                                    }
                                    else if (teamScores[sup][1] < teamScores[curr][1])
                                    {
                                        sup = curr;
                                    }
                                }
                                else if (teamScores[sup][6] < teamScores[curr][6])
                                {
                                    sup = curr;
                                }
                            } 
                            else if (teamScores[sup][5] < teamScores[curr][5])
                            {
                                sup = curr;
                            }
                        } 
                        else if (teamScores[sup][2] < teamScores[curr][2])
                        {
                            sup = curr;
                        }
                    } 
                    else if (teamScores[sup][0] <  teamScores[curr][0])
                    {
                        sup = curr;
                    }
                }
                finalInfo[count] = TextFormat(sup, teamScores[sup], count);
                count++;
                tempList.Remove(sup);
            }
            /*foreach (var key in teamScores.Keys)
            {
                Console.WriteLine($"{key} - {teamScores[key][0]}, {teamScores[key][1]}");
            }*/
            return finalInfo;
        }

        static string TextFormat(string name, int[] s, int place)
        {
            //Console.WriteLine($"{place}) {name} {s[0]}p, {s[1]}g ({s[2]}-{s[3]}-{s[4]}), {s[5]}gd ({s[6]}-{s[7]})");
            return ($"{place}) {name} {s[0]}p, {s[1]}g ({s[2]}-{s[3]}-{s[4]}), {s[5]}gd ({s[6]}-{s[7]})");
        }

        static string[] Breakdown(string jumble)
        {
            string temp = "";
            // [team1, goals1, goals2, team2]
            List<string> match = new List<string>();
            foreach (char c in jumble)
            {
                if (c == '#' || c == '@')
                {
                    match.Add(temp);
                    temp = "";
                }
                else
                {
                    temp += c;
                }
            }

            if (temp != "")
            {
                match.Add(temp);
            }

            //Console.WriteLine($"\n{match[0]} {match[1]} {match[2]} {match[3]}\n");
            return match.ToArray();
        }
        
        
        static void Main(string[] args)
        {
            /*
            string team1 = "South Africa#1@1#Mexico";
            */
            string[] input = new string[]
            {
                "Liga BBVA",
                "Atletico Madrid#1@1#FC Barcelona Jr",
                "FC Barcelona#1@1#Atletico Madrid Jr"
            };
            string[] rankings = (getRankings(input));
            foreach (string rank in rankings)
            {
                Console.WriteLine(rank);
            }
            {
                
            }
        }
    }
}
