---
layout: default
title: "Assessing Large Language Models on Islamic Legal Reasoning: Evidence from Inheritance Law Evaluation"
---

# Assessing Large Language Models on Islamic Legal Reasoning: Evidence from Inheritance Law Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01081" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01081v2</a>
  <a href="https://arxiv.org/pdf/2509.01081.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01081v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01081v2', 'Assessing Large Language Models on Islamic Legal Reasoning: Evidence from Inheritance Law Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abdessalam Bouchekif, Samer Rashwani, Heba Sbahi, Shahd Gaben, Mutaz Al-Khatib, Mohammed Ghaly

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-01 (更新: 2025-09-17)

**备注**: 10 pages, 7 Tables, Code: https://github.com/bouchekif/inheritance_evaluation

**🔗 代码/项目**: [GITHUB](https://github.com/bouchekif/inheritance_evaluation)

---

## 💡 一句话要点

**评估大型语言模型在伊斯兰继承法推理中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `伊斯兰法律` `继承法` `推理能力` `错误分析` `法律智能化`

## 📋 核心要点

1. 现有大型语言模型在处理伊斯兰继承法时存在显著的推理能力差异，部分模型表现不佳。
2. 通过设计1,000道多项选择题的基准测试，评估模型在理解和计算继承法则方面的能力。
3. 实验结果显示，部分模型准确率低于50%，而其他模型则超过90%，揭示了推理能力的显著差异。

## 📝 摘要（中文）

本文评估了大型语言模型在伊斯兰继承法（'ilm al-mawarith）中的知识和推理能力。通过1,000道多项选择题的基准测试，评估七种语言模型在不同继承场景下的表现，旨在测试模型理解继承背景和计算法定份额的能力。结果显示，o3和Gemini 2.5的准确率超过90%，而ALLaM、Fanar、LLaMA和Mistral的得分低于50%。这些差异反映了推理能力和领域适应性的重要差异。我们进行了详细的错误分析，识别出模型在理解继承场景、法律规则应用不当和领域知识不足等方面的重复失败模式。研究结果突显了在结构化法律推理中的局限性，并提出了改进伊斯兰法律推理表现的方向。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在伊斯兰继承法推理中的表现不足，尤其是在理解复杂法律场景和应用法律规则方面的挑战。现有方法在处理结构化法律推理时存在明显局限。

**核心思路**：通过构建一个包含多样化继承场景的基准测试，评估模型的推理能力和领域适应性，旨在识别模型的强项与弱点，从而为改进提供依据。

**技术框架**：整体架构包括数据集构建、模型评估和错误分析三个主要模块。首先，设计多项选择题以涵盖不同的继承场景；其次，使用七种大型语言模型进行评估；最后，分析模型的错误类型和原因。

**关键创新**：本研究的创新点在于首次系统性地评估大型语言模型在特定法律领域的推理能力，特别是伊斯兰继承法的应用，填补了这一领域的研究空白。

**关键设计**：在模型评估中，采用了多项选择题的形式，确保问题涵盖法律规则的多样性，并通过详细的错误分析识别模型在法律推理中的具体不足。

## 📊 实验亮点

实验结果显示，o3和Gemini 2.5在伊斯兰继承法的推理任务中准确率超过90%，而ALLaM、Fanar、LLaMA和Mistral的准确率均低于50%。这些结果揭示了不同模型在法律推理能力上的显著差异，并为未来的改进提供了方向。

## 🎯 应用场景

该研究的潜在应用领域包括法律教育、法律咨询和智能法律服务等。通过提升大型语言模型在法律推理中的表现，可以为法律从业者提供更为精准的辅助工具，进而提高法律服务的效率和准确性。未来，该研究可能推动更多领域的法律智能化进程。

## 📄 摘要（原文）

> This paper evaluates the knowledge and reasoning capabilities of Large Language Models in Islamic inheritance law, known as 'ilm al-mawarith. We assess the performance of seven LLMs using a benchmark of 1,000 multiple-choice questions covering diverse inheritance scenarios, designed to test models' ability to understand the inheritance context and compute the distribution of shares prescribed by Islamic jurisprudence. The results reveal a significant performance gap: o3 and Gemini 2.5 achieved accuracies above 90%, whereas ALLaM, Fanar, LLaMA, and Mistral scored below 50%. These disparities reflect important differences in reasoning ability and domain adaptation. We conduct a detailed error analysis to identify recurring failure patterns across models, including misunderstandings of inheritance scenarios, incorrect application of legal rules, and insufficient domain knowledge. Our findings highlight limitations in handling structured legal reasoning and suggest directions for improving performance in Islamic legal reasoning. Code: https://github.com/bouchekif/inheritance_evaluation

