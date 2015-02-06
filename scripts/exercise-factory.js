/**
* Add-on to exercise class to construct exercises.
* Depends on exercise.js and all its subclasses.
*
* @author Carlos Rodriguez Dominguez
*/

if (!Exercise.getInstance) {

Exercise.getInstance = function(sessionID, exerciseID, repetition, exerciseEntry)
{
	var e = null;
	
	switch(parseInt(exerciseEntry.type))
	{
		// Memory
		case 1:
			e = new NumbersAndVowelsExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
		case 2:
			e = new TaskListExercise(sessionID, exerciseID, repetition, exerciseEntry, false);
			break;
		case 3:
			e = new ClassifyObjectsExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
		case 18:
			e = new TaskListExercise(sessionID, exerciseID, repetition, exerciseEntry, true);
			break;
		case 19:
			e = new WordListExercise(sessionID, exerciseID, repetition, exerciseEntry, true);
			break;
		case 7:
			e = new DirectNumbersExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
		case 8:
			e = new WordListExercise(sessionID, exerciseID, repetition, exerciseEntry, false);
			break;
		case 25:
			e = new PositionsExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
			
		// Attention
		case 4:
			e = new BalloonsExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
		case 5:
			e = new BagItemsExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
		case 6:
			e = new PyramidsExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
		case 9:
			e = new LostItemsExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
			
		// Reasoning exercises
		case 11:
			e = new SemanticSeriesExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
		case 12:
			e = new LogicalSeriesExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;				
		case 13:
			e = new SpatialReasoningExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;				
		case 14:
			e = new ClassifyExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
		case 15:
			e = new SemanticAnalogiesExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
	
		// Planning
		case 16:
			e = new GiftShoppingExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
		case 17:
			e = new PackageDeliveryExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
		case 20:
			e = new VRExercise(sessionID, exerciseID, repetition, exerciseEntry, true);
			break;
		case 21:
			e = new VRExercise(sessionID, exerciseID, repetition, exerciseEntry, false);
			break;
			
		// Tests
		case 30:
			e = new QuestionnaireExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
			
		case 32:
			//e = new MouseDialogExercice(sessionID, exerciseID, repetition, exerciseEntry);
			break;
			
		case 33:
			e = new InstrumentalQuestionnaireExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
			
		// Helps
		case 34:
			e = new IntroductionExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
			
		case 101:
			e = new FirstHelpExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
	
		case 102:
			e = new SecondHelpExercise(sessionID, exerciseID, repetition, exerciseEntry);
			break;
	}
	
	if (!e) //create dummy exercise
	{
		e = new DummyExercise(sessionID, exerciseID, repetition, exerciseEntry);
	}
	
	return e;
};

}