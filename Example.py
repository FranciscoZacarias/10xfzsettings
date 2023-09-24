#------------------------------------------------------------------------
import N10X

#------------------------------------------------------------------------
# this function is bound to Alt-H and prints "Hello World!" to the 10x Output window
def HelloWorld():
    print("Hello World!");

#------------------------------------------------------------------------
def ExecuteVSCommandTest():
    N10X.Editor.ExecuteVSCommand("File.NewFile")

#------------------------------------------------------------------------
def ToggleColumnCount():
    column_count = N10X.Editor.GetColumnCount()
    if column_count == 1:
        column_count = 2
    else:
        column_count = 1
    N10X.Editor.SetColumnCount(column_count)

#------------------------------------------------------------------------
# shows how to use the N10X interface to insert text in the current text editor
def InsertText(text):
    N10X.Editor.InsertText(text)

#################
# NOTE(fz): Custom fz commands.

def DeleteToEndOfLineAndSaveToClipboard():
	# Unlike the DeleteToEndOfLine command, this copies the deleted section to the clipboard
	x, y = N10X.Editor.GetCursorPos()
	N10X.Editor.SetSelection((x, y), (len(N10X.Editor.GetLine(y)), y), 0)
	N10X.Editor.ExecuteCommand("Cut")

def GoToNextEmptyLineUp():
	x, current_line = N10X.Editor.GetCursorPos()
	current_line -= 1 # Start on the previous line

	while len(N10X.Editor.GetLine(current_line).strip()) > 0:
		current_line -= 1
	N10X.Editor.SetCursorPos((0, current_line))

def GoToNextEmptyLineDown():
	x, current_line = N10X.Editor.GetCursorPos()
	current_line += 1 # Start on the next line

	while len(N10X.Editor.GetLine(current_line).strip()) > 0:
		current_line += 1
	N10X.Editor.SetCursorPos((0, current_line))
