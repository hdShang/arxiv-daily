---
layout: default
title: A Video Is Not Worth a Thousand Words
---

# A Video Is Not Worth a Thousand Words

**arXiv**: [2510.23253v1](https://arxiv.org/abs/2510.23253) | [PDF](https://arxiv.org/pdf/2510.23253.pdf)

**作者**: Sam Pollard, Michael Wray

---

## 💡 一句话要点

**提出基于Shapley值的特征归因与模态评分方法，评估多模态模型在视频问答中的文本依赖问题。**

**关键词**: `视频问答` `多模态模型` `Shapley值` `特征归因` `模态交互` `文本依赖`

## 📋 核心要点

1. 核心问题：多模态模型在视频问答中可能过度依赖文本，忽略视频模态的交互。
2. 方法要点：使用Shapley值计算特征归因和模态分数，支持任意定义特征和模态。
3. 实验或效果：比较6个模型在4个数据集上，发现模型倾向于忽略干扰项，依赖文本。

## 📄 摘要（原文）

> As we become increasingly dependent on vision language models (VLMs) to
> answer questions about the world around us, there is a significant amount of
> research devoted to increasing both the difficulty of video question answering
> (VQA) datasets, and the context lengths of the models that they evaluate. The
> reliance on large language models as backbones has lead to concerns about
> potential text dominance, and the exploration of interactions between
> modalities is underdeveloped. How do we measure whether we're heading in the
> right direction, with the complexity that multi-modal models introduce? We
> propose a joint method of computing both feature attributions and modality
> scores based on Shapley values, where both the features and modalities are
> arbitrarily definable. Using these metrics, we compare $6$ VLM models of
> varying context lengths on $4$ representative datasets, focusing on
> multiple-choice VQA. In particular, we consider video frames and whole textual
> elements as equal features in the hierarchy, and the multiple-choice VQA task
> as an interaction between three modalities: video, question and answer. Our
> results demonstrate a dependence on text and show that the multiple-choice VQA
> task devolves into a model's ability to ignore distractors. Code available at
> https://github.com/sjpollard/a-video-is-not-worth-a-thousand-words.

