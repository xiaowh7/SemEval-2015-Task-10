/**
 * Created by seven on 10/31/14.
 */
import java.io.*;
import java.util.*;

import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.ling.Sentence;
import edu.stanford.nlp.trees.*;
import edu.stanford.nlp.parser.lexparser.LexicalizedParser;

public class dependencyParser {
    public static void main(String[] args) throws IOException {
        LexicalizedParser lp =
                LexicalizedParser.loadModel(
                        "edu/stanford/nlp/models/lexparser/englishRNN.ser.gz");

        String infile = args[0];
        BufferedReader reader = new BufferedReader(new FileReader(infile));
        String outfile = args[1];
        BufferedWriter writer = new BufferedWriter(new FileWriter(outfile));

        String nextLine;
        int cnt = 0;

        while ((nextLine = reader.readLine()) != null){
            cnt++;
            if (cnt%100==0) System.out.println(cnt);

            String tokenString = nextLine.split("\t")[0];
            List<String> tokenList = new ArrayList<String>();
            String[] tokens = tokenString.split(" ");
            for(int i=0; i<tokens.length; i++){
                if (tokens[i].startsWith("@") ||
                        tokens[i].startsWith("http://") ||
                        tokens[i].startsWith("https://"))
                    continue;
                tokenList.add(tokens[i]);
            }

            String[] tokenProcessed = tokenList.toArray(new String[tokenList.size()]);
            List<CoreLabel> rawWords = Sentence.toCoreLabelList(tokenProcessed);
            Tree parse = lp.apply(rawWords);
            TreebankLanguagePack tlp = lp.getOp().langpack();
            GrammaticalStructureFactory gsf = tlp.grammaticalStructureFactory();
            GrammaticalStructure gs = gsf.newGrammaticalStructure(parse);

            Collection<TypedDependency> tdl = gs.allTypedDependencies();
            Object[] ans = tdl.toArray();
            for (int i=0;i<ans.length;i++){
                writer.write(ans[i].toString());
                writer.write("\t");
            }
            writer.write("\n");
        }

        reader.close();
        writer.close();
    }
}
