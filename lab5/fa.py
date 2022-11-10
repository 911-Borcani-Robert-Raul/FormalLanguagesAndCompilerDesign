class FiniteAutomaton:
    """
    This class contains functionalities related to finite automaton.
    """

    def __init__(self, set_of_states, alphabet, transition_function, initial_state, final_states):
        """
        Creates a new finite automaton, using given set of states, alphabet, transition function, initial state and final states.
        Parameters:
            :set_of_states: an array of the states of the finite automaton
            :alphabet: an array of characters denoting the alphabet
            :transition_function: the transition function for the FA. It is a dictionary that maps each state to an array of tuples,
                                    each tuple being constructed from the next state, together with the symbol from the alphabet
            :initial_state: the state that will be considered as the initial state
            :final_states: an array of the states that will be final states
        """
        self._set_of_states = set_of_states
        self._alphabet = alphabet
        self._transition_function = transition_function
        self._initial_state = initial_state
        self._final_states = final_states
    
    def get_set_of_states(self):
        """
        Gets the set of states:
        Return value:
            An array of strings denoting the set of states for the finite automaton.
        """
        return self._set_of_states
    
    def get_alphabet(self):
        """
        Gets the alphabet of the FA.
        Return value:
            An array of characters, denoting the alphabet for this FA.
        """
        return self._alphabet
    
    def get_transitions(self):
        """
        Gets the set of transitions for the FA
        Return value:
            a dictionary that maps each state to an array of tuples, each tuple being constructed from the next state,
            together with the symbol from the alphabet
        """
        return self._transition_function
    
    def get_initial_state(self):
        """
        Gets the initial state.
        Return value:
            A string denoting the name of the initial state
        """
        return self._initial_state
    
    def get_final_states(self):
        """
        Gets the set of final states.
        Return value:
            An array of strings denoting the set of final states
        """
        return self._final_states

    def init_from_file(file_name):
        """
        Initializes a new FA, by reading the data about it from a file.

        Structure of the file:
        Line 1: state0, state1, ... - set of all states, separated by space
        Line 2: ABC... - alphabet, as a string (array of characters)
        Line 3: N - number of transitions
        Lines 4 ... 4 + N - 1: qi qf s1 s2 ... - transition from state qi to qf by symbols s1, s2, ... from the alphabet
        Line 4 + N: initial_state - the initial state
        Lines 4 + N + 1: qf0, qf1, ... - set of final states, separated by spaces

        Parameters:
            :file_name: The name of the file containing information about the FA
        Return value:
            A new FiniteAutomata object constructed based on information from the provided file.
        """
        with open(file_name) as file:
            states = file.readline().strip().split(' ')
            alphabet = file.readline()

            n = int(file.readline())
            transitions = {}
            for state in states:
                transitions[state] = {}

            for _ in range(n):
                transition = file.readline().strip().split(' ')
                for symbol in transition[2]:
                    transitions[transition[0]][symbol] = transition[1]
            
            initial_state = file.readline().strip()
            final_states = file.readline().strip().split(' ')

            return FiniteAutomaton(states, alphabet, transitions, initial_state, final_states)
    
    def __str__(self):
        return f"""
        Set of states: {self._set_of_states}
        Alphabet: {self._alphabet}
        Transitions: {self._transition_function}
        Initial state: {self._initial_state}
        Set of final states: {self._final_states}
        """
    
    def _check(self, word, state):
        if word == '':
            return state in self._final_states
        if word[0] not in self._transition_function[state]:
            return False
        return self._check(word[1:], self._transition_function[state][word[0]])
    
    def check_word(self, word):
        """
        Checks if a word is accepted by the finite automaton
        Parameters:
            :word: a string - the word to be checked
        Return value:
            True if the word is accepted, False otherwise
        """
        return self._check(word, self._initial_state)

