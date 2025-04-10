%%%%%%%%%%%%%%%%%%% D O  N O T  D E L E T E %%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%                                                            %%
%%  BulSU BS Math Thesis                                      %%
%%  LateX Template (bulsuthesis.cls)                          %%
%%  Version 4 (4 November 2024)                               %%
%%                                                            %%
%%  When used as documentclass of thesis.tex,			      %%
%%  this class will implement the format and layout of	      %%
%%  the BS Mathematics undergraduate thesis of                %%
%%  the Collge of Science, Bulacan State University.          %%
%%                                                            %%
%%  Original Author:                                          %%
%%  Harris R. Dela Cruz                                       %%
%%  Bulacan State University                                  %%
%%  e-mail: harris.delacruz@bulsu.edu.ph                      %%
%%                                                            %%
%%  Permission: Any student of the University is hereby given %%
%%  permission to use this template and the accompanying 	  %%
%%  Thesis.tex and thesis-structure.tex files provided	      %%
%%  the original author is given due acknwledgement.		  %%
%%                                                            %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%% D O  N O T  D E L E T E %%%%%%%%%%%%%%%%%%%%

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{bulsuthesis}[2024/11/04 v4.0 Bulacan Sate University csthesis class (H.R. Dela Cruz)]

\DeclareOption*{%% Load the report class with the 12pt option
	\PassOptionsToClass{\CurrentOption}{report}
}
\ProcessOptions\relax
\LoadClass[12pt]{report}

%----------------------------------------------------------------
% REQUIRED PACKAGES
%----------------------------------------------------------------
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{setspace}
\RequirePackage{pdfpages}		%for inserting pdf files
\RequirePackage{url}				%for typesetting url
\RequirePackage{epsfig,graphicx}	%for inserting image file
\RequirePackage{amsmath,amssymb,amsthm} %for math equations
\RequirePackage{chngcntr}
\RequirePackage{pbox,framed}		%for boxes
\RequirePackage{calligra}		%font for dedication
\RequirePackage[shortlabels]{enumitem} % Customize lists
\RequirePackage{bookmark}
\RequirePackage{titlesec} 
\RequirePackage[titles]{tocloft}
\RequirePackage{etoolbox}
\RequirePackage{appendix}		%for inserting appendices


%----------------------------------------------------------------
% PAGE LAYOUT
%----------------------------------------------------------------
\RequirePackage{geometry}	%for paper sizes/dimensions
\geometry{
	top=1in,left=1.5in,right=1in,bottom=1in,
	headheight=15pt,
	footskip=36pt,
}

\RequirePackage{indentfirst}	%indent first sentence
\setlength{\parindent}{5ex}	%change the length of indentation


\RequirePackage{fancyhdr}	%tweaking header and footer
	\pagestyle{fancy}
		\fancyhf{}
		\fancyhead[L]{\itshape\leftmark}
		\fancyhead[R]{\thepage}
		\renewcommand{\headrulewidth}{0pt}
	\fancypagestyle{plain}{%pagestyle with no header
		\fancyhf{}% Clear header/footer
		\fancyfoot[C]{\thepage}
		\renewcommand{\headrulewidth}{0pt}%
		}%

\newcommand{\clearemptydoublepage}{\newpage{\pagestyle{plain}\cleardoublepage}}


%---------------------------------------------------------------
% ADDITIONAL THESIS SECTIONS
%---------------------------------------------------------------
\renewenvironment{abstract}%
{\chapter*{ABSTRACT}
	\addcontentsline{toc}{chapter}{ABSTRACT}
	\begingroup
}{\newpage\endgroup}

\newenvironment{acknowledgment}%
{\chapter*{ACKNOWLEDGMENT}
	\addcontentsline{toc}{chapter}{ACKNOWLEDGMENT}
	\begingroup
}{\clearpage\endgroup}

\newenvironment{dedication}%
{\chapter*{DEDICATION}
	\addcontentsline{toc}{chapter}{DEDICATION}
	\begingroup
}{\clearpage\endgroup}

\newenvironment{listofnotations}%
{\chapter*{LIST OF NOTATIONS}
	\addcontentsline{toc}{chapter}{LIST OF NOTATIONS}
	\begingroup
}{\clearpage\endgroup}

\newenvironment{curriculumvitae}%
{\addcontentsline{toc}{chapter}{CURRICULUM VITAE}
	\begingroup
	\clearpage
	\centering\pagestyle{plain}
	\mbox{}\vfill
	{\Huge\bfseries CURRICULUM VITAE}
	\vfill
	\pagebreak
}{\clearpage\endgroup}



\newenvironment{preliminary}%
{\pagestyle{plain}\pagenumbering{roman}}%
{\pagenumbering{arabic}}




%----------------------------------------------------------------
% APPENDIX ENVIRONMENT
%----------------------------------------------------------------
\newcommand{\listappendixname}{LIST OF APPENDICES}
\newlistof{appendix}{apc}{\listappendixname}

\AtBeginEnvironment{appendices}{%
  \clearpage
  \setcounter{table}{0}
  \setcounter{figure}{0}
  \renewcommand\thefigure{\thechapter.\arabic{figure}} 
  \renewcommand\thetable{\thechapter.\arabic{table}}
  
%  \makeatletter
  \def\@chapter[#1]#2{\ifnum \c@secnumdepth >\m@ne
  	\refstepcounter{chapter}%
  	\typeout{\@chapapp\space\thechapter.}%
  	\addcontentsline{toc}{chapter}%
  	{\protect\numberline{\thechapter}\texorpdfstring{{#1}}{#1}}%
  	\else
  	\addcontentsline{toc}{chapter}{\texorpdfstring{{#1}}{#1}}%
  	\fi
  	\chaptermark{#1}%
  	\addtocontents{lof}{\protect\addvspace{10\p@}}%
  	\addtocontents{lot}{\protect\addvspace{10\p@}}%
  	\if@twocolumn
  	\@topnewpage[\@makechapterhead{#2}]%
  	\else
  	\@makechapterhead{#2}%
  	\@afterheading
  	\fi}
%  \makeatother
  
  {\centering\thispagestyle{empty}
  	\addcontentsline{toc}{chapter}{APPENDICES}
  	\mbox{}\vfill
  	{\Huge\bfseries APPENDICES}
  	\vfill
  }
  
  \write\@auxout{%
    \string\let\string\latex@tf@toc\string\tf@toc% Store the original `\tf@toc` file handle
    \string\let\string\tf@toc\string\tf@apc% 
  }% Naughty trick
}

\AtEndEnvironment{appendices}{%
  \write\@auxout{%
    \string\let\string\tf@toc\string\latex@tf@toc% 
  }% Naughty trick, restoring the old `\tf@toc` number, to be able to write stuff to the real `.toc` again.
}


%This will remove chapter-related separation in the list environment tables and figures
\usepackage{etoolbox}% http://ctan.org/pkg/etoolbox
\newcommand*{\noaddvspace}{\renewcommand*{\addvspace}[1]{}}
\addtocontents{lof}{\protect\noaddvspace}
\addtocontents{lot}{\protect\noaddvspace}
\addtocontents{apc}{\protect\noaddvspace}

\let\oldcontentsline\contentsline
\newcommand{\nopagecontentsline}[3]{\oldcontentsline{#1}{#2}{}}


%---------------------------------------------------------------
% BASIC INFORMATION AND DEGREE SPECIFICATION
%---------------------------------------------------------------
\newcommand{\college}[1]{\ifx\empty#1\else\gdef\@college{#1}\fi}
\newcommand{\csdean}[1]{\ifx\empty#1\else\gdef\@csdean{#1}\fi}
\newcommand{\papertype}[1]{\ifx\empty#1\else\gdef\@papertype{#1}\fi}
\newcommand{\degree}[1]{\ifx\empty#1\else\gdef\@degree{#1}\fi}
\newcommand{\specialization}[1]{\ifx\empty#1\else\gdef\@specialization{#1}\fi}
\newcommand{\adviser}[1]{\ifx\empty#1\else\gdef\@adviser{#1}\fi}
\newcommand{\advisersuffix}[1]{\ifx\empty#1\else\gdef\@advisersuffix{#1}\fi}
\newcommand{\panelchair}[1]{\ifx\empty#1\else\gdef\@panelchair{#1}\fi}
\newcommand{\paneltwo}[1]{\ifx\empty#1\else\gdef\@paneltwo{#1}\fi}
\newcommand{\panelthree}[1]{\ifx\empty#1\else\gdef\@panelthree{#1}\fi}
\newcommand{\ddate}[1]{\ifx\empty#1\else\gdef\@ddate{#1}\fi}

\renewcommand{\author}[1]{\ifx\empty#1\else\gdef\@author{#1}\fi}
\renewcommand{\title}[1]{\ifx\empty#1\else\gdef\@title{#1}\fi}
\newcommand{\fronttitle}[1]{\ifx\empty#1\else\gdef\@fronttitle{#1}\fi}

\newcommand{\authorone}[1]{\ifx\empty#1\else\gdef\@authorone{#1}\fi}
\newcommand{\authortwo}[1]{\ifx\empty#1\else\gdef\@authortwo{#1}\fi}
\newcommand{\authorthree}[1]{\ifx\empty#1\else\gdef\@authorthree{#1}\fi}
\newcommand{\authorfour}[1]{\ifx\empty#1\else\gdef\@authorfour{#1}\fi}
\newcommand{\authorfive}[1]{\ifx\empty#1\else\gdef\@authorfive{#1}\fi}

%---------------------------------------------------------------
% DEFAULT VALUES
%---------------------------------------------------------------
\global\def\@college{\mbox{College of Science}} % Default is College of Science
\global\def\@csdean{\mbox{Name CS Dean}}

\global\def\@papertype{\mbox{Thesis}} % Default is Thesis
\global\def\@degree{Bachelor of Science in Mathematics} % Default is BS Math
\global\def\@specialization{Computer Science}

\global\def\@title{\mbox{Title of a Thesis}}
\global\def\@fronttitle{\mbox{Title of a Thesis}}
\global\def\@author{\mbox{Author's Name}}
\global\def\@authorone{\mbox{}}
\global\def\@authortwo{\mbox{}}
\global\def\@authorthree{\mbox{}}
\global\def\@authorfour{\mbox{}}
\global\def\@authorfive{\mbox{}}
\global\def\@ddate{\ifcase\the\month\or January\or
	February\or March\or April\or May\or June\or July\or August\or
	September\or October\or November\or December\fi\space \number\the\year} % Default date is current date
\global\def\@adviser{\mbox{Thesis Adviser}}
\global\def\@advisersuffix{\mbox{}}
\global\def\@panelchair{\mbox{Panel Chair}}
\global\def\@paneltwo{\mbox{Panel Member 2}}
\global\def\@panelthree{\mbox{Panel Member 3}}

%---------------------------------------------------------------
% TITLE PAGE - Change \maketitle to follow the guidelines
%---------------------------------------------------------------
\renewcommand{\maketitle}
{\begin{titlepage}
		\addcontentsline{toc}{chapter}{TITLE PAGE}
		\setcounter{page}{1}
		%% Set the line spacing to 1 for the title page.
		\begin{center}
			\makebox(\linewidth,1in)[t]{\parbox{\linewidth}{\centering \usefont{T1}{qhv}{b}{n}\selectfont\large\MakeUppercase\@fronttitle}}
			
			\vspace{1in}
			
			An Undergraduate {\@papertype} Presented to\\
			the Faculty of the {\@college}\\
			of the Bulacan State University\\
			City of Malolos, Bulacan
			
			\vfill
			
			In Partial Fulfillment of the Requirements for the Degree\\
			{\@degree} with \\
			Specialization in {\@specialization}\\
			
			\vfill
			
			by \\
			{\MakeUppercase{\@author}}\\
			
			\vfill
			
			under the supervision of \\
			{\MakeUppercase{\@adviser}}\@advisersuffix\\
			
			\vfill
			
			{\@ddate}
		\end{center}
	\end{titlepage}
	\setcounter{page}{2}
}

%---------------------------------------------------------------
%  APPROVAL SHEET
%---------------------------------------------------------------
\def\approvalsheet{%
	\chapter*{APPROVAL SHEET}
	\label{approvalsheet}
	\addcontentsline{toc}{chapter}{APPROVAL SHEET}
	\thispagestyle{empty}
	
	In partial fulfillment of the requirements for the degree {\@degree} with specialization in {\@specialization}, this thesis entitled {\bfseries\MakeUppercase``\@title''} has been prepared and submitted by \@authorone, \@authortwo, \@authorthree, \@authorfour\ and \@authorfive\ who are hereby recommended for oral examination.
	
	\vspace{1em}
	
	{\singlespacing 
		\hfill \pbox{5in}{\relax\ifvmode\centering\fi \textbf{\MakeUppercase{\@adviser}} \\ Adviser}
	}
	
	\vspace{\stretch{1}}
	
	The document is approved in partial fulfillment of the requirements for the degree {\@degree} with specialization in {\@specialization} by the Committee on Oral Examination.
	
	\vspace{1em}
	
	{\singlespacing \centering
		\pbox{5in}{\relax\ifvmode\centering\fi%
			\textbf{\MakeUppercase{\@panelchair}} \\ Chairperson
		}
		
		\vspace{2em}
		
		\pbox{2.5in}{\relax\ifvmode\centering\fi%
			\textbf{\MakeUppercase{\@paneltwo}} \\ Member
		}
		\hfill 
		\pbox{2.5in}{\relax\ifvmode\centering\fi%
			\textbf{\MakeUppercase{\@panelthree}} \\ Member
		}
	}
	
	\vspace{\stretch{1}}
	
	The document is accepted and approved in partial fulfillment of the requirements for the degree {\@degree} with specialization in {\@specialization} by the Committee on Oral Examination. 
	
	\vspace{1em	}
	
	{\singlespacing \centering
		\hfill \pbox{5in}{\relax\ifvmode\centering\fi%
			\textbf{\@csdean} \\ Dean, College of Science
		}
	}
	
	\vspace{\stretch{1}}
	
	\noindent\textbf{\@ddate}
	\clearpage
	
	%-------------------------
}
