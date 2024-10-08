# {
#             "role": "system",
#             "content": "문제를 해결하는 과정을 단계별로 명확하게 설명한 다음, 최종 답변을 제시해 주세요.",
#         },

PROMPT_STRATEGY = {
    "cot-1-shot": [
        {
            "role": "user",
            "content": '''문제를 해결하는 과정을 단계별로 명확하게 설명한 다음, 최종 답변을 제시해 주세요.

한 도시에서 매년 나무를 심고 있습니다. 첫해에 100그루를 심었고, 매년 전년도에 심은 나무의 수보다 20%씩 더 많은 나무를 심고 있습니다. 2년 후에는 총 몇 그루의 나무를 심게 될까요?''',
        },
        {
            "role": "assistant",
            "content": """이 문제를 해결하기 위해 단계별로 접근해 보겠습니다.

1단계: 주어진 정보 정리
- 첫해에 100그루를 심음
- 매년 전년도보다 20% 더 많은 나무를 심음
- 2년 후의 총 나무 수를 구해야 함

2단계: 두 번째 해에 심은 나무 수 계산
- 첫해보다 20% 증가
- 100 + (100의 20%) = 100 + 20 = 120그루

3단계: 세 번째 해에 심은 나무 수 계산
- 두 번째 해보다 20% 증가
- 120 + (120의 20%) = 120 + 24 = 144그루

4단계: 3년 동안 심은 총 나무 수 계산
- 첫해: 100그루
- 둘째 해: 120그루
- 셋째 해: 144그루
- 총합: 100 + 120 + 144 = 364그루

따라서, 2년 후(즉, 3년째)에는 총 364그루의 나무를 심게 됩니다.""",
        },
    ],
    "1-shot": [
        {
            "role": "user",
            "content": "Git의 rebase와 merge의 차이점을 설명하고, 각각 어떤 상황에서 사용하는 것이 좋은지 예를 들어 설명해주세요.",
        },
        {
            "role": "assistant",
            "content": """Git에서 `rebase`와 `merge`는 두 개의 브랜치를 통합하는 데 사용되는 두 가지 주요 명령어입니다. 이들의 차이점과 사용 상황을 설명하겠습니다.

### Rebase

#### 개념
- `rebase`는 하나의 브랜치의 커밋을 다른 브랜치의 끝에 다시 적용하는 것입니다. 즉, 커밋 히스토리를 새로 만든다고 할 수 있습니다.
- 결과적으로 커밋 히스토리가 깔끔하게 정리됩니다.

#### 사용 상황
- **깔끔한 히스토리가 필요할 때**: 브랜치 히스토리가 병합 없이 일직선으로 이어지도록 하고 싶을 때 유용합니다.
- **작업 중인 브랜치를 최신 상태로 유지하고 싶을 때**: 예를 들어, `feature` 브랜치에서 작업 중인데 `main` 브랜치에서 업데이트가 있을 경우, `feature` 브랜치를 `rebase`하여 최신 상태로 유지할 수 있습니다.

#### 예제
1. `feature` 브랜치에서 작업 중입니다.
2. `main` 브랜치에 새로운 커밋이 추가되었습니다.
3. `feature` 브랜치에서 `git rebase main`을 실행합니다.
4. `feature` 브랜치의 커밋들이 `main` 브랜치의 최신 커밋들 뒤에 재배치됩니다.

```bash
git checkout feature
git rebase main
```

### Merge

#### 개념
- `merge`는 두 개의 브랜치를 합치는 방법으로, 두 브랜치의 히스토리를 유지하며 새로운 병합 커밋을 생성합니다.
- `merge`는 기존의 히스토리를 그대로 보존합니다.

#### 사용 상황
- **히스토리를 유지하고 싶을 때**: 각 브랜치의 작업 기록을 그대로 보존하면서 병합할 때 사용합니다.
- **협업 중 충돌을 명확히 해결하고 기록을 남기고 싶을 때**: 여러 사람이 같은 저장소에서 작업할 때, `merge`는 충돌 해결 과정과 그 기록을 명확히 남길 수 있습니다.

#### 예제
1. `feature` 브랜치에서 작업을 완료했습니다.
2. `main` 브랜치에 병합하고 싶습니다.
3. `main` 브랜치로 체크아웃한 후 `feature` 브랜치를 병합합니다.

```bash
git checkout main
git merge feature
```

### 요약

- **Rebase**는 히스토리를 깔끔하게 정리하는 데 유리하며, 주로 개인 작업이나 `feature` 브랜치를 최신 상태로 유지할 때 사용됩니다.
- **Merge**는 두 브랜치의 작업 히스토리를 보존하면서 병합하며, 협업 과정에서 충돌 해결과 기록을 명확히 남기는 데 유리합니다.

각 방법의 장단점과 사용 상황을 고려하여 적절히 선택하는 것이 중요합니다.""",
        },
    ],
    "default": [],
}

JUDGE_TEMPLATE = {
    "single_turn": """너는 질문에 대한 한국어 언어 모델의 답변을 매우 꼼꼼히 평가할 것이다. 공정한 평가를 위해 아래의 규칙을 준수한다.

# 기본 규칙
1. 질문의 요구사항을 충분히 반영하였는지 상세히 분석할 것.
2. 답변 과정에서 누락되었거나 포함되지 못하여 아쉬운 부분에 대하여 상세히 분석할 것.
3. 답변의 길이가 평가 결과에 영향을 미치지 않도록 할 것.
4. Additional Reference가 제공된다면 평가 시 해당 정보를 참고할 것.

# 언어 요구사항
- 모델은 반드시 한국어로 답변해야 하며, 다른 언어로의 답변은 절대 허용되지 않는다.
- 예외적으로 질문이 영어로 답변할 것을 요구할 때에만 영어 답변이 허용된다.
- 한국어로 답변하지 않을 경우, 점수는 0점 처리된다.
- 언어 요구사항을 충족하는 것은 필수적이나, 이 요구사항의 충족이 답변의 질적 평가에 추가 점수로 이어지지는 않는다.

# 평가 출력 방식
**주어진 Question에 집중하여** Model's Response에 대한 평가와 1~10의 점수를 부여한다. 답변에 대한 평가는 4~5 문장으로 규칙을 참고하여 상세히 작성한다.

# 출력 형식
평가: 평가 내용
점수: 숫자""",
    "multi_turn": """너는 대화 후 이어지는 후속 질문에 대한 한국어 언어 모델의 답변을 매우 꼼꼼히 평가할 것이다. 공정한 평가를 위해 아래의 규칙을 준수한다.

# 기본 규칙
1. 질문의 요구사항을 충분히 반영하였는지 상세히 분석할 것.
2. 답변 과정에서 누락되었거나 포함되지 못하여 아쉬운 부분에 대하여 상세히 분석할 것.
3. 답변의 길이가 평가 결과에 영향을 미치지 않도록 할 것.
4. Additional Reference가 제공된다면 평가 시 해당 정보를 참고할 것.
5. 후속 질문에 대한 답변이 이전 대화 맥락과 일치하는지 확인할 것.

# 언어 요구사항
- 모델은 반드시 한국어로 답변해야 하며, 다른 언어로의 답변은 절대 허용되지 않는다.
- 예외적으로 질문이 영어로 답변할 것을 요구할 때에만 영어 답변이 허용된다.
- 한국어로 답변하지 않을 경우, 점수는 0점 처리된다.
- 언어 요구사항을 충족하는 것은 필수적이나, 이 요구사항의 충족이 답변의 질적 평가에 추가 점수로 이어지지는 않는다.

# 평가 출력 방식
**주어진 Question에 집중하여** Model's Response에 대한 평가와 1~10의 점수를 부여한다. 답변에 대한 평가는 4~5 문장으로 규칙을 참고하여 상세히 작성한다.

# 출력 형식
평가: 평가 내용
점수: 숫자""",
}
