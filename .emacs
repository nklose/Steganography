;; Emacs configuration file for Nick Klose (nick.klose@ualberta.ca)
(custom-set-variables '(inhibit-startup-screen t))
(custom-set-faces)

;; Use standard keys for copy/paste/undo
(cua-mode)                             

;; Use the F12 key to compile
(global-set-key [f12] 'compile)        

;; Use abbreviations
(setq-default abbrev-mode t)           
(read-abbrev-file "~/.abbrev_defs")
(setq save-abbrevs t)

;; Highlight the line the cursor is currently on
(global-hl-line-mode 1)

;; Scroll line-by-line to prevent cursor from jumping around
(setq scroll-step 1)

;; Replace all tabs with four spaces
(setq-default indent-tabs-mode nil)

;; Treat new buffers as text files
(setq default-major-mode 'text-mode)

;; Function to delete an entire line
;; Code from http://homepages.inf.ed.ac.uk/s0243221/emacs/

;; First define a variable which will store the previous column position
(defvar previous-column nil "Save the column position")

;; Define the nuke-line function. The line is killed, then the newline
;; character is deleted. The column which the cursor was positioned at is then
;; restored. Because the kill-line function is used, the contents deleted can
;; be later restored by usibackward-delete-char-untabifyng the yank commands.
(defun nuke-line()
  "Kill an entire line, including the trailing newline character"
  (interactive)

  ;; Store the current column position, so it can later be restored for a more
  ;; natural feel to the deletion
  (setq previous-column (current-column))

  ;; Now move to the end of the current line
  (end-of-line)

  ;; Test the length of the line. If it is 0, there is no need for a
  ;; kill-line. All that happens in this case is that the new-line character
  ;; is deleted.
  (if (= (current-column) 0)
    (delete-char 1)

    ;; This is the 'else' clause. The current line being deleted is not zero
    ;; in length. First remove the line by moving to its start and then
    ;; killing, followed by deletion of the newline character, and then
    ;; finally restoration of the column position.
    (progn
      (beginning-of-line)
      (kill-line)
      (delete-char 1)
      (move-to-column previous-column))))

;; Now bind the delete line function to the F10 key
(global-set-key [f10] 'nuke-line)
