export interface ReviewResponse {
  answer: string;
}

export interface FunctionMatch {
  file: string;
  line: number;
  class: string | null;
  signature: string;
  language: string;
  code: string;
}

export interface SummaryResponse {
  summary: string;
}