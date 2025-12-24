---
layout: default
title: "NurValues: Real-World Nursing Values Evaluation for Large Language Models in Clinical Context"
---

# NurValues: Real-World Nursing Values Evaluation for Large Language Models in Clinical Context

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08734" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08734v1</a>
  <a href="https://arxiv.org/pdf/2505.08734.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08734v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08734v1', 'NurValues: Real-World Nursing Values Evaluation for Large Language Models in Clinical Context')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ben Yao, Qiuchi Li, Yazhou Zhang, Siyu Yang, Bohan Zhang, Prayag Tiwari, Jing Qin

**分类**: cs.CL

**发布日期**: 2025-05-13

**备注**: 25 pages, 10 figures, 16 tables

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/Ben012345)

---

## 💡 一句话要点

**提出NurValues基准以评估临床环境中的护理价值对齐**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `护理价值对齐` `大型语言模型` `伦理评估` `对抗样本` `临床环境` `数据集构建` `深度学习` `医疗人工智能`

## 📋 核心要点

1. 现有方法在护理价值对齐评估中缺乏系统性基准，难以有效衡量大型语言模型的伦理表现。
2. 本研究提出了NurValues基准，通过真实护理行为实例和对话格式的对抗样本，系统评估护理价值对齐。
3. 实验结果显示，DeepSeek-V3在Easy-Level数据集上表现最佳，而Claude 3.5 Sonnet在Hard-Level数据集上超越其他模型，揭示了护理价值评估的复杂性。

## 📝 摘要（中文）

本研究首次引入护理价值对齐的基准，涵盖来自国际护理规范的五个核心价值维度：利他主义、人类尊严、诚信、公正和专业精神。该基准包含通过为期五个月的纵向实地研究收集的1,100个真实护理行为实例，并由五名临床护士进行标注。每个原始案例与一个价值对齐和一个价值违反的版本配对，形成2,200个标记实例，构成Easy-Level数据集。为了增加对抗复杂性，每个实例进一步转化为对话格式，嵌入上下文线索和微妙的误导信号，形成Hard-Level数据集。我们评估了23个最先进的LLM在护理价值对齐方面的表现，发现深度学习模型在Easy-Level数据集上表现最佳，而Claude 3.5 Sonnet在Hard-Level数据集上超越其他模型，显著优于医疗LLM。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有护理价值对齐评估方法缺乏系统性基准的问题，现有方法无法有效衡量大型语言模型在临床环境中的伦理表现。

**核心思路**：通过构建NurValues基准，结合真实护理行为实例和对话格式的对抗样本，系统性地评估大型语言模型的护理价值对齐能力。

**技术框架**：整体架构包括数据收集、标注、对抗样本生成和模型评估四个主要模块。数据收集通过纵向实地研究获取真实护理行为，标注由临床护士完成，对抗样本则通过生成反向伦理极性的实例实现。

**关键创新**：本研究的核心创新在于首次构建了护理价值对齐的系统性基准，并通过对话格式增强了数据集的复杂性，使得评估更具挑战性和现实意义。

**关键设计**：在数据集构建中，设置了Easy-Level和Hard-Level两个难度层次，采用了对话格式以嵌入上下文线索和误导信号，确保模型在真实场景中的表现得到有效评估。实验中使用了23个最先进的LLM进行对比分析，确保结果的可靠性和有效性。

## 📊 实验亮点

实验结果显示，DeepSeek-V3在Easy-Level数据集上取得了94.55的最高性能，而Claude 3.5 Sonnet在Hard-Level数据集上以89.43的成绩显著超越其他模型，尤其是在评估护理价值维度中，公正性始终是最难以评估的维度，表明了在上下文学习中显著提升对齐能力的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗人工智能、护理教育和伦理决策支持系统。通过提供一个系统性的护理价值对齐基准，可以帮助开发更具伦理意识的语言模型，提升临床决策的质量与安全性，促进护理实践的标准化与规范化。

## 📄 摘要（原文）

> This work introduces the first benchmark for nursing value alignment, consisting of five core value dimensions distilled from international nursing codes: Altruism, Human Dignity, Integrity, Justice, and Professionalism. The benchmark comprises 1,100 real-world nursing behavior instances collected through a five-month longitudinal field study across three hospitals of varying tiers. These instances are annotated by five clinical nurses and then augmented with LLM-generated counterfactuals with reversed ethic polarity. Each original case is paired with a value-aligned and a value-violating version, resulting in 2,200 labeled instances that constitute the Easy-Level dataset. To increase adversarial complexity, each instance is further transformed into a dialogue-based format that embeds contextual cues and subtle misleading signals, yielding a Hard-Level dataset. We evaluate 23 state-of-the-art (SoTA) LLMs on their alignment with nursing values. Our findings reveal three key insights: (1) DeepSeek-V3 achieves the highest performance on the Easy-Level dataset (94.55), where Claude 3.5 Sonnet outperforms other models on the Hard-Level dataset (89.43), significantly surpassing the medical LLMs; (2) Justice is consistently the most difficult nursing value dimension to evaluate; and (3) in-context learning significantly improves alignment. This work aims to provide a foundation for value-sensitive LLMs development in clinical settings. The dataset and the code are available at https://huggingface.co/datasets/Ben012345/NurValues.

