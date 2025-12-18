---
layout: default
title: Yes-MT's Submission to the Low-Resource Indic Language Translation Shared Task in WMT 2024
---

# Yes-MT's Submission to the Low-Resource Indic Language Translation Shared Task in WMT 2024

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15226" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15226v1</a>
  <a href="https://arxiv.org/pdf/2512.15226.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15226v1" onclick="toggleFavorite(this, '2512.15226v1', 'Yes-MT\'s Submission to the Low-Resource Indic Language Translation Shared Task in WMT 2024')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yash Bhaskar, Parameswari Krishnamurthy

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-17

**备注**: Accepted at WMT 2024

**期刊**: In Proceedings of the Ninth Conference on Machine Translation (WMT 2024), pages 788-792, 2024

**DOI**: [10.18653/v1/2024.wmt-1.71](https://doi.org/10.18653/v1/2024.wmt-1.71)

---

## 💡 一句话要点

**Yes-MT团队探索多种模型和微调策略，解决WMT 2024低资源印度语言翻译难题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低资源翻译` `印度语言` `机器翻译` `预训练模型` `LoRA微调`

## 📋 核心要点

1. 低资源印度语言翻译面临数据稀缺的挑战，严重制约了翻译模型的性能。
2. 探索了包括微调预训练模型、LoRA微调、LLM提示以及从头训练Transformer等多种方法。
3. 实验结果表明，LLM结合微调策略在低资源翻译任务中具有潜力，但仍面临挑战。

## 📝 摘要（中文）

本文介绍了Yes-MT团队在WMT 2024低资源印度语言翻译共享任务中的提交系统，重点关注英语与阿萨姆语、米佐语、卡西语和曼尼普尔语之间的翻译。实验探索了多种方法，包括在多语言和单语言设置中微调预训练模型，如mT5和IndicBart；使用LoRA微调IndicTrans2；使用大型语言模型（LLM），如Llama 3和Mixtral 8x7b进行零样本和少样本提示；Llama 3的LoRA监督微调；以及从头开始训练Transformer模型。使用SacreBLEU和CHRF在WMT23低资源印度语言翻译共享任务测试数据上评估了结果，突出了低资源翻译的挑战以及LLM在这些任务中的潜力，特别是通过微调。

## 🔬 方法详解

**问题定义**：论文旨在解决低资源场景下，英语与阿萨姆语、米佐语、卡西语和曼尼普尔语等印度语言之间的翻译问题。现有方法在这些资源匮乏的语言上表现不佳，难以达到令人满意的翻译质量。

**核心思路**：论文的核心思路是利用预训练模型（如mT5、IndicBart、IndicTrans2）的知识迁移能力，结合微调技术（如LoRA）和LLM的上下文学习能力，从而在低资源条件下提升翻译性能。同时，也探索了从头训练Transformer模型的可行性。

**技术框架**：整体框架包括以下几个主要阶段：1) 数据预处理：对低资源语言数据进行清洗和整理。2) 模型选择与配置：选择合适的预训练模型或Transformer架构。3) 微调或训练：使用低资源数据对模型进行微调（如LoRA）或从头训练。4) 推理：使用训练好的模型进行翻译。5) 评估：使用SacreBLEU和CHRF等指标评估翻译质量。

**关键创新**：论文的关键创新在于对多种模型和微调策略的综合探索，并分析了它们在低资源印度语言翻译任务中的表现。特别是在LLM的应用方面，尝试了零样本、少样本提示以及LoRA监督微调等方法，为后续研究提供了参考。

**关键设计**：论文中涉及的关键设计包括：1) 预训练模型的选择：根据语言相似性和模型规模选择合适的预训练模型。2) LoRA微调参数设置：调整LoRA的秩（rank）和学习率等参数，以平衡模型性能和训练效率。3) LLM提示策略：设计有效的提示语，引导LLM生成高质量的翻译结果。4) 损失函数：使用交叉熵损失函数训练模型。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15226v1/structured_output.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在低资源印度语言翻译任务中，微调预训练模型和利用LLM的提示学习具有潜力。虽然没有给出具体的性能数据和提升幅度，但强调了这些方法在解决低资源翻译问题上的价值，并为未来的研究方向提供了指导。

## 🎯 应用场景

该研究成果可应用于低资源语言的机器翻译系统，促进跨文化交流和信息共享。例如，可以用于开发支持阿萨姆语、米佐语等印度语言的翻译工具，帮助当地居民获取更多信息，也可以用于构建多语言的教育资源和文化产品。未来，该研究方向有望推动低资源语言的数字化和保护。

## 📄 摘要（原文）

> This paper presents the systems submitted by the Yes-MT team for the Low-Resource Indic Language Translation Shared Task at WMT 2024 (Pakray et al., 2024), focusing on translating between English and the Assamese, Mizo, Khasi, and Manipuri languages. The experiments explored various approaches, including fine-tuning pre-trained models like mT5 (Xue et al., 2020) and IndicBart (Dabre et al., 2021) in both multilingual and monolingual settings, LoRA (Hu et al., 2021) fine-tuning IndicTrans2 (Gala et al., 2023), zero-shot and few-shot prompting (Brown, 2020) with large language models (LLMs) like Llama 3 (Dubey et al., 2024) and Mixtral 8x7b (Jiang et al., 2024), LoRA supervised fine-tuning of Llama 3 (Mecklenburg et al., 2024), and training Transformer models (Vaswani, 2017) from scratch. The results were evaluated on the WMT23 Low-Resource Indic Language Translation Shared Task test data using SacreBLEU (Post, 2018) and CHRF (Popovic, 2015), highlighting the challenges of low-resource translation and the potential of LLMs for these tasks, particularly with fine-tuning.

