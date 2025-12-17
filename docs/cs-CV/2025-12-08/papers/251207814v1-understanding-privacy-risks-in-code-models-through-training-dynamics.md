---
layout: default
title: Understanding Privacy Risks in Code Models Through Training Dynamics: A Causal Approach
---

# Understanding Privacy Risks in Code Models Through Training Dynamics: A Causal Approach

**arXiv**: [2512.07814v1](https://arxiv.org/abs/2512.07814) | [PDF](https://arxiv.org/pdf/2512.07814.pdf)

**作者**: Hua Yang, Alejandro Velasco, Sen Fang, Bowen Xu, Denys Poshyvanyk

---

## 💡 一句话要点

**提出基于训练动态的因果方法，揭示代码模型中不同类型PII的隐私泄露风险差异。**

**关键词**: `代码大模型` `隐私风险` `训练动态` `因果推断` `PII类型` `泄露分析`

## 📋 核心要点

1. 核心问题：代码大模型依赖开源库，可能泄露PII，但现有研究忽视不同类型PII的异质风险。
2. 方法要点：构建多类型PII数据集，微调不同规模模型，计算训练动态，并建立结构因果模型评估因果效应。
3. 实验或效果：结果显示PII泄露风险因类型而异，易学类型如IP地址泄露更高，难学类型如密钥泄露较少。

## 📄 摘要（原文）

> Large language models for code (LLM4Code) have greatly improved developer productivity but also raise privacy concerns due to their reliance on open-source repositories containing abundant personally identifiable information (PII). Prior work shows that commercial models can reproduce sensitive PII, yet existing studies largely treat PII as a single category and overlook the heterogeneous risks among different types. We investigate whether distinct PII types vary in their likelihood of being learned and leaked by LLM4Code, and whether this relationship is causal. Our methodology includes building a dataset with diverse PII types, fine-tuning representative models of different scales, computing training dynamics on real PII data, and formulating a structural causal model to estimate the causal effect of learnability on leakage. Results show that leakage risks differ substantially across PII types and correlate with their training dynamics: easy-to-learn instances such as IP addresses exhibit higher leakage, while harder types such as keys and passwords leak less frequently. Ambiguous types show mixed behaviors. This work provides the first causal evidence that leakage risks are type-dependent and offers guidance for developing type-aware and learnability-aware defenses for LLM4Code.

