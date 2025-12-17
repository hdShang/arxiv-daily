---
layout: default
title: Beyond the Pixels: VLM-based Evaluation of Identity Preservation in Reference-Guided Synthesis
---

# Beyond the Pixels: VLM-based Evaluation of Identity Preservation in Reference-Guided Synthesis

**arXiv**: [2511.08087v1](https://arxiv.org/abs/2511.08087) | [PDF](https://arxiv.org/pdf/2511.08087.pdf)

**作者**: Aditi Singhania, Krutik Malani, Riddhi Dhawan, Arushi Jain, Garv Tandon, Nippun Sharma, Souymodip Chakraborty, Vineet Batra, Ankit Phogat

---

## 💡 一句话要点

**提出基于VLM的分层评估框架以解决生成模型中身份保持的细粒度评估问题**

**关键词**: `身份保持评估` `视觉语言模型` `分层评估框架` `生成模型基准` `细粒度分析`

## 📋 核心要点

1. 核心问题：现有指标依赖全局嵌入或粗略提示，无法捕捉细粒度身份变化且诊断能力有限
2. 方法要点：通过分层分解主体为决策树，引导VLM进行结构化推理以评估特征级变换
3. 实验或效果：在四个先进生成模型上验证，与人类判断高度一致，并引入新基准

## 📄 摘要（原文）

> Evaluating identity preservation in generative models remains a critical yet unresolved challenge. Existing metrics rely on global embeddings or coarse VLM prompting, failing to capture fine-grained identity changes and providing limited diagnostic insight. We introduce Beyond the Pixels, a hierarchical evaluation framework that decomposes identity assessment into feature-level transformations. Our approach guides VLMs through structured reasoning by (1) hierarchically decomposing subjects into (type, style) -> attribute -> feature decision tree, and (2) prompting for concrete transformations rather than abstract similarity scores. This decomposition grounds VLM analysis in verifiable visual evidence, reducing hallucinations and improving consistency. We validate our framework across four state-of-the-art generative models, demonstrating strong alignment with human judgments in measuring identity consistency. Additionally, we introduce a new benchmark specifically designed to stress-test generative models. It comprises 1,078 image-prompt pairs spanning diverse subject types, including underrepresented categories such as anthropomorphic and animated characters, and captures an average of six to seven transformation axes per prompt.

