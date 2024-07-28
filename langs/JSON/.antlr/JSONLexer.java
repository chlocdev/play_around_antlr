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
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, STRING=7, NUMBER=8, TRUE=9, 
		FALSE=10, NULL=11, WS=12;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "DIGIT", "ESCAPE", "UNICODE", 
			"HEX", "STRING", "NUMBER", "INT", "EXP", "TRUE", "FALSE", "NULL", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'{'", "','", "'}'", "':'", "'['", "']'", null, null, "'true'", 
			"'false'", "'null'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, "STRING", "NUMBER", "TRUE", 
			"FALSE", "NULL", "WS"
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
		"\u0004\u0000\f\u0083\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u00077\b"+
		"\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t"+
		"\u0001\n\u0001\n\u0001\n\u0005\nD\b\n\n\n\f\nG\t\n\u0001\n\u0001\n\u0001"+
		"\u000b\u0003\u000bL\b\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0004"+
		"\u000bQ\b\u000b\u000b\u000b\f\u000bR\u0003\u000bU\b\u000b\u0001\u000b"+
		"\u0003\u000bX\b\u000b\u0001\f\u0001\f\u0001\f\u0005\f]\b\f\n\f\f\f`\t"+
		"\f\u0003\fb\b\f\u0001\r\u0001\r\u0003\rf\b\r\u0001\r\u0004\ri\b\r\u000b"+
		"\r\f\rj\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0004"+
		"\u0011~\b\u0011\u000b\u0011\f\u0011\u007f\u0001\u0011\u0001\u0011\u0000"+
		"\u0000\u0012\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b"+
		"\u0006\r\u0000\u000f\u0000\u0011\u0000\u0013\u0000\u0015\u0007\u0017\b"+
		"\u0019\u0000\u001b\u0000\u001d\t\u001f\n!\u000b#\f\u0001\u0000\u0007\b"+
		"\u0000\"\"//\\\\bbffnnrrtt\u0003\u000009AFaf\u0004\u0000\n\n\r\r\"\"\\"+
		"\\\u0001\u000019\u0002\u0000EEee\u0002\u0000++--\u0003\u0000\t\n\r\r "+
		" \u0088\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000"+
		"\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000"+
		"\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000"+
		"\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000"+
		"\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000"+
		"\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0001%"+
		"\u0001\u0000\u0000\u0000\u0003\'\u0001\u0000\u0000\u0000\u0005)\u0001"+
		"\u0000\u0000\u0000\u0007+\u0001\u0000\u0000\u0000\t-\u0001\u0000\u0000"+
		"\u0000\u000b/\u0001\u0000\u0000\u0000\r1\u0001\u0000\u0000\u0000\u000f"+
		"3\u0001\u0000\u0000\u0000\u00118\u0001\u0000\u0000\u0000\u0013>\u0001"+
		"\u0000\u0000\u0000\u0015@\u0001\u0000\u0000\u0000\u0017K\u0001\u0000\u0000"+
		"\u0000\u0019a\u0001\u0000\u0000\u0000\u001bc\u0001\u0000\u0000\u0000\u001d"+
		"l\u0001\u0000\u0000\u0000\u001fq\u0001\u0000\u0000\u0000!w\u0001\u0000"+
		"\u0000\u0000#}\u0001\u0000\u0000\u0000%&\u0005{\u0000\u0000&\u0002\u0001"+
		"\u0000\u0000\u0000\'(\u0005,\u0000\u0000(\u0004\u0001\u0000\u0000\u0000"+
		")*\u0005}\u0000\u0000*\u0006\u0001\u0000\u0000\u0000+,\u0005:\u0000\u0000"+
		",\b\u0001\u0000\u0000\u0000-.\u0005[\u0000\u0000.\n\u0001\u0000\u0000"+
		"\u0000/0\u0005]\u0000\u00000\f\u0001\u0000\u0000\u000012\u000209\u0000"+
		"2\u000e\u0001\u0000\u0000\u000036\u0005\\\u0000\u000047\u0007\u0000\u0000"+
		"\u000057\u0003\u0011\b\u000064\u0001\u0000\u0000\u000065\u0001\u0000\u0000"+
		"\u00007\u0010\u0001\u0000\u0000\u000089\u0005u\u0000\u00009:\u0003\u0013"+
		"\t\u0000:;\u0003\u0013\t\u0000;<\u0003\u0013\t\u0000<=\u0003\u0013\t\u0000"+
		"=\u0012\u0001\u0000\u0000\u0000>?\u0007\u0001\u0000\u0000?\u0014\u0001"+
		"\u0000\u0000\u0000@E\u0005\"\u0000\u0000AD\u0003\u000f\u0007\u0000BD\b"+
		"\u0002\u0000\u0000CA\u0001\u0000\u0000\u0000CB\u0001\u0000\u0000\u0000"+
		"DG\u0001\u0000\u0000\u0000EC\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000"+
		"\u0000FH\u0001\u0000\u0000\u0000GE\u0001\u0000\u0000\u0000HI\u0005\"\u0000"+
		"\u0000I\u0016\u0001\u0000\u0000\u0000JL\u0005-\u0000\u0000KJ\u0001\u0000"+
		"\u0000\u0000KL\u0001\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000MT\u0003"+
		"\u0019\f\u0000NP\u0005.\u0000\u0000OQ\u0003\r\u0006\u0000PO\u0001\u0000"+
		"\u0000\u0000QR\u0001\u0000\u0000\u0000RP\u0001\u0000\u0000\u0000RS\u0001"+
		"\u0000\u0000\u0000SU\u0001\u0000\u0000\u0000TN\u0001\u0000\u0000\u0000"+
		"TU\u0001\u0000\u0000\u0000UW\u0001\u0000\u0000\u0000VX\u0003\u001b\r\u0000"+
		"WV\u0001\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000X\u0018\u0001\u0000"+
		"\u0000\u0000Yb\u00050\u0000\u0000Z^\u0007\u0003\u0000\u0000[]\u0003\r"+
		"\u0006\u0000\\[\u0001\u0000\u0000\u0000]`\u0001\u0000\u0000\u0000^\\\u0001"+
		"\u0000\u0000\u0000^_\u0001\u0000\u0000\u0000_b\u0001\u0000\u0000\u0000"+
		"`^\u0001\u0000\u0000\u0000aY\u0001\u0000\u0000\u0000aZ\u0001\u0000\u0000"+
		"\u0000b\u001a\u0001\u0000\u0000\u0000ce\u0007\u0004\u0000\u0000df\u0007"+
		"\u0005\u0000\u0000ed\u0001\u0000\u0000\u0000ef\u0001\u0000\u0000\u0000"+
		"fh\u0001\u0000\u0000\u0000gi\u0003\r\u0006\u0000hg\u0001\u0000\u0000\u0000"+
		"ij\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000jk\u0001\u0000\u0000"+
		"\u0000k\u001c\u0001\u0000\u0000\u0000lm\u0005t\u0000\u0000mn\u0005r\u0000"+
		"\u0000no\u0005u\u0000\u0000op\u0005e\u0000\u0000p\u001e\u0001\u0000\u0000"+
		"\u0000qr\u0005f\u0000\u0000rs\u0005a\u0000\u0000st\u0005l\u0000\u0000"+
		"tu\u0005s\u0000\u0000uv\u0005e\u0000\u0000v \u0001\u0000\u0000\u0000w"+
		"x\u0005n\u0000\u0000xy\u0005u\u0000\u0000yz\u0005l\u0000\u0000z{\u0005"+
		"l\u0000\u0000{\"\u0001\u0000\u0000\u0000|~\u0007\u0006\u0000\u0000}|\u0001"+
		"\u0000\u0000\u0000~\u007f\u0001\u0000\u0000\u0000\u007f}\u0001\u0000\u0000"+
		"\u0000\u007f\u0080\u0001\u0000\u0000\u0000\u0080\u0081\u0001\u0000\u0000"+
		"\u0000\u0081\u0082\u0006\u0011\u0000\u0000\u0082$\u0001\u0000\u0000\u0000"+
		"\r\u00006CEKRTW^aej\u007f\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}