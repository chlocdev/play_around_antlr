// Generated from /home/loc/Workspaces/play_around_antlr/langs/JSON/JSON.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class JSONLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		STRING=10, NUMBER=11, WS=12;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"STRING", "ESC", "NUMBER", "INT", "EXP", "WS", "HEX"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'true'", "'false'", "'null'", "'{'", "','", "'}'", "':'", "'['", 
			"']'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "STRING", 
			"NUMBER", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public JSONLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "JSON.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\f|\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\t\u0005\tA\b\t\n\t\f\tD\t\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\nP\b\n\u0001\u000b\u0003"+
		"\u000bS\b\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0004\u000bX\b\u000b"+
		"\u000b\u000b\f\u000bY\u0003\u000b\\\b\u000b\u0001\u000b\u0003\u000b_\b"+
		"\u000b\u0001\f\u0001\f\u0001\f\u0005\fd\b\f\n\f\f\fg\t\f\u0003\fi\b\f"+
		"\u0001\r\u0001\r\u0003\rm\b\r\u0001\r\u0004\rp\b\r\u000b\r\f\rq\u0001"+
		"\u000e\u0004\u000eu\b\u000e\u000b\u000e\f\u000ev\u0001\u000e\u0001\u000e"+
		"\u0001\u000f\u0001\u000f\u0000\u0000\u0010\u0001\u0001\u0003\u0002\u0005"+
		"\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n"+
		"\u0015\u0000\u0017\u000b\u0019\u0000\u001b\u0000\u001d\f\u001f\u0000\u0001"+
		"\u0000\b\u0002\u0000\"\"\\\\\b\u0000\"\"//\\\\bbffnnrrtt\u0001\u00000"+
		"9\u0001\u000019\u0002\u0000EEee\u0002\u0000++--\u0003\u0000\t\n\r\r  "+
		"\u0003\u000009AFaf\u0083\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003"+
		"\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007"+
		"\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001"+
		"\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000"+
		"\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000"+
		"\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000"+
		"\u0000\u0000\u0001!\u0001\u0000\u0000\u0000\u0003&\u0001\u0000\u0000\u0000"+
		"\u0005,\u0001\u0000\u0000\u0000\u00071\u0001\u0000\u0000\u0000\t3\u0001"+
		"\u0000\u0000\u0000\u000b5\u0001\u0000\u0000\u0000\r7\u0001\u0000\u0000"+
		"\u0000\u000f9\u0001\u0000\u0000\u0000\u0011;\u0001\u0000\u0000\u0000\u0013"+
		"=\u0001\u0000\u0000\u0000\u0015G\u0001\u0000\u0000\u0000\u0017R\u0001"+
		"\u0000\u0000\u0000\u0019h\u0001\u0000\u0000\u0000\u001bj\u0001\u0000\u0000"+
		"\u0000\u001dt\u0001\u0000\u0000\u0000\u001fz\u0001\u0000\u0000\u0000!"+
		"\"\u0005t\u0000\u0000\"#\u0005r\u0000\u0000#$\u0005u\u0000\u0000$%\u0005"+
		"e\u0000\u0000%\u0002\u0001\u0000\u0000\u0000&\'\u0005f\u0000\u0000\'("+
		"\u0005a\u0000\u0000()\u0005l\u0000\u0000)*\u0005s\u0000\u0000*+\u0005"+
		"e\u0000\u0000+\u0004\u0001\u0000\u0000\u0000,-\u0005n\u0000\u0000-.\u0005"+
		"u\u0000\u0000./\u0005l\u0000\u0000/0\u0005l\u0000\u00000\u0006\u0001\u0000"+
		"\u0000\u000012\u0005{\u0000\u00002\b\u0001\u0000\u0000\u000034\u0005,"+
		"\u0000\u00004\n\u0001\u0000\u0000\u000056\u0005}\u0000\u00006\f\u0001"+
		"\u0000\u0000\u000078\u0005:\u0000\u00008\u000e\u0001\u0000\u0000\u0000"+
		"9:\u0005[\u0000\u0000:\u0010\u0001\u0000\u0000\u0000;<\u0005]\u0000\u0000"+
		"<\u0012\u0001\u0000\u0000\u0000=B\u0005\"\u0000\u0000>A\u0003\u0015\n"+
		"\u0000?A\b\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000@?\u0001\u0000\u0000"+
		"\u0000AD\u0001\u0000\u0000\u0000B@\u0001\u0000\u0000\u0000BC\u0001\u0000"+
		"\u0000\u0000CE\u0001\u0000\u0000\u0000DB\u0001\u0000\u0000\u0000EF\u0005"+
		"\"\u0000\u0000F\u0014\u0001\u0000\u0000\u0000GO\u0005\\\u0000\u0000HP"+
		"\u0007\u0001\u0000\u0000IJ\u0005u\u0000\u0000JK\u0003\u001f\u000f\u0000"+
		"KL\u0003\u001f\u000f\u0000LM\u0003\u001f\u000f\u0000MN\u0003\u001f\u000f"+
		"\u0000NP\u0001\u0000\u0000\u0000OH\u0001\u0000\u0000\u0000OI\u0001\u0000"+
		"\u0000\u0000P\u0016\u0001\u0000\u0000\u0000QS\u0005-\u0000\u0000RQ\u0001"+
		"\u0000\u0000\u0000RS\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000"+
		"T[\u0003\u0019\f\u0000UW\u0005.\u0000\u0000VX\u0007\u0002\u0000\u0000"+
		"WV\u0001\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000YW\u0001\u0000\u0000"+
		"\u0000YZ\u0001\u0000\u0000\u0000Z\\\u0001\u0000\u0000\u0000[U\u0001\u0000"+
		"\u0000\u0000[\\\u0001\u0000\u0000\u0000\\^\u0001\u0000\u0000\u0000]_\u0003"+
		"\u001b\r\u0000^]\u0001\u0000\u0000\u0000^_\u0001\u0000\u0000\u0000_\u0018"+
		"\u0001\u0000\u0000\u0000`i\u00050\u0000\u0000ae\u0007\u0003\u0000\u0000"+
		"bd\u0007\u0002\u0000\u0000cb\u0001\u0000\u0000\u0000dg\u0001\u0000\u0000"+
		"\u0000ec\u0001\u0000\u0000\u0000ef\u0001\u0000\u0000\u0000fi\u0001\u0000"+
		"\u0000\u0000ge\u0001\u0000\u0000\u0000h`\u0001\u0000\u0000\u0000ha\u0001"+
		"\u0000\u0000\u0000i\u001a\u0001\u0000\u0000\u0000jl\u0007\u0004\u0000"+
		"\u0000km\u0007\u0005\u0000\u0000lk\u0001\u0000\u0000\u0000lm\u0001\u0000"+
		"\u0000\u0000mo\u0001\u0000\u0000\u0000np\u0007\u0002\u0000\u0000on\u0001"+
		"\u0000\u0000\u0000pq\u0001\u0000\u0000\u0000qo\u0001\u0000\u0000\u0000"+
		"qr\u0001\u0000\u0000\u0000r\u001c\u0001\u0000\u0000\u0000su\u0007\u0006"+
		"\u0000\u0000ts\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000\u0000vt\u0001"+
		"\u0000\u0000\u0000vw\u0001\u0000\u0000\u0000wx\u0001\u0000\u0000\u0000"+
		"xy\u0006\u000e\u0000\u0000y\u001e\u0001\u0000\u0000\u0000z{\u0007\u0007"+
		"\u0000\u0000{ \u0001\u0000\u0000\u0000\r\u0000@BORY[^ehlqv\u0001\u0006"+
		"\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}