---
layout: default
title: "LLMCARE: early detection of cognitive impairment via transformer models enhanced by LLM-generated synthetic data"
---

# LLMCARE: early detection of cognitive impairment via transformer models enhanced by LLM-generated synthetic data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10027" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10027v3</a>
  <a href="https://arxiv.org/pdf/2508.10027.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10027v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10027v3', 'LLMCARE: early detection of cognitive impairment via transformer models enhanced by LLM-generated synthetic data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ali Zolnour, Hossein Azadmaleki, Yasaman Haghbin, Fatemeh Taherinezhad, Mohamad Javad Momeni Nezhad, Sina Rashidi, Masoud Khani, AmirSajjad Taleban, Samin Mahdizadeh Sani, Maryam Dadkhah, James M. Noble, Suzanne Bakken, Yadollah Yaghoobzadeh, Abdol-Hossein Vahabie, Masoud Rouhizadeh, Maryam Zolnoori

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-08 (更新: 2025-11-10)

**DOI**: [10.3389/frai.2025.1669896](https://doi.org/10.3389/frai.2025.1669896)

---

## 💡 一句话要点

**提出LLMCARE以解决早期认知障碍检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `认知障碍检测` `自然语言处理` `变换器模型` `合成数据增强` `多模态学习` `阿尔茨海默病` `机器学习`

## 📋 核心要点

1. 现有方法在早期识别阿尔茨海默病及相关痴呆症方面存在不足，许多患者未能及时诊断。
2. 本研究提出了一种结合变换器嵌入和手工语言特征的语音筛查管道，并利用LLM生成的合成数据进行增强。
3. 实验结果表明，融合模型在ADReSSo数据集上取得了F1=83.3的成绩，显著优于基线方法，且在独立MCI队列上验证了其潜力。

## 📝 摘要（中文）

阿尔茨海默病及相关痴呆症（ADRD）在美国影响近五百万老年人，但超过一半未被诊断。基于语音的自然语言处理（NLP）提供了一种可扩展的方法，通过微妙的语言标记检测早期认知衰退。本研究开发并评估了一种语音筛查管道，结合了变换器嵌入、手工语言特征、使用大型语言模型（LLMs）生成的合成数据增强，以及单模态和多模态分类器的基准测试。外部验证评估了其在仅有轻度认知障碍（MCI）队列中的泛化能力。

## 🔬 方法详解

**问题定义**：本研究旨在解决早期认知障碍的检测问题，现有方法在识别微妙的语言标记方面存在局限，导致许多患者未能及时诊断。

**核心思路**：论文提出了一种结合变换器模型和手工语言特征的筛查管道，并通过大型语言模型生成合成数据进行增强，以提高检测的准确性和效率。

**技术框架**：整体架构包括数据收集、特征提取、模型训练和评估四个主要阶段。首先，从ADReSSo和DementiaBank Delaware数据集中提取语音转录，然后结合变换器嵌入和语言特征进行特征融合，最后使用不同的分类器进行性能评估。

**关键创新**：最重要的技术创新在于将LLM生成的合成数据与传统的语言特征相结合，显著提升了模型的检测能力，并在多模态模型的应用中探索了新的可能性。

**关键设计**：在实验中，使用了十种变换器模型和三种多模态LLM，采用了不同的微调策略。融合模型结合了来自顶级变换器的嵌入和110个语言特征，优化了模型的性能。

## 📊 实验亮点

在ADReSSo数据集上，融合模型的F1得分达到83.3（AUC=89.5），显著优于仅使用变换器和语言特征的基线模型。使用MedAlpaca7B生成的合成数据增强后，F1得分提升至85.7，显示出数据增强的有效性。独立MCI队列验证支持了该筛查管道的临床相关性。

## 🎯 应用场景

该研究的潜在应用领域包括老年医学、心理健康筛查和公共卫生。通过早期识别认知障碍，能够为患者提供及时的干预和治疗，改善生活质量。此外，该方法的可扩展性使其适用于大规模筛查，具有重要的社会价值。

## 📄 摘要（原文）

> Alzheimer's disease and related dementias(ADRD) affect nearly five million older adults in the United States, yet more than half remain undiagnosed. Speech-based natural language processing(NLP) offers a scalable approach for detecting early cognitive decline through subtle linguistic markers that may precede clinical diagnosis. This study develops and evaluates a speech-based screening pipeline integrating transformer embeddings with handcrafted linguistic features, synthetic augmentation using large language models(LLMs), and benchmarking of unimodal and multimodal classifiers. External validation assessed generalizability to a MCI-only cohort.
>   Transcripts were drawn from the ADReSSo 2021 benchmark dataset(n=237, Pitt Corpus) and the DementiaBank Delaware corpus(n=205, MCI vs. controls). Ten transformer models were tested under three fine-tuning strategies. A late-fusion model combined embeddings from the top transformer with 110 linguistic features. Five LLMs(LLaMA8B/70B, MedAlpaca7B, Ministral8B,GPT-4o) generated label-conditioned synthetic speech for augmentation, and three multimodal LLMs(GPT-4o,Qwen-Omni,Phi-4) were evaluated in zero-shot and fine-tuned modes. On ADReSSo, the fusion model achieved F1=83.3(AUC=89.5), outperforming transformer-only and linguistic baselines. MedAlpaca7B augmentation(2x) improved F1=85.7, though larger scales reduced gains. Fine-tuning boosted unimodal LLMs(MedAlpaca7B F1=47.7=>78.7), while multimodal models performed lower (Phi-4=71.6;GPT-4o=67.6). On Delaware, the fusion plus 1x MedAlpaca7B model achieved F1=72.8(AUC=69.6). Integrating transformer and linguistic features enhances ADRD detection. LLM-based augmentation improves data efficiency but yields diminishing returns, while current multimodal models remain limited. Validation on an independent MCI cohort supports the pipeline's potential for scalable, clinically relevant early screening.

