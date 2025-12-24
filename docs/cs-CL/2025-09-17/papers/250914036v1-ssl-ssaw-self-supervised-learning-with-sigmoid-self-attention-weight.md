---
layout: default
title: "SSL-SSAW: Self-Supervised Learning with Sigmoid Self-Attention Weighting for Question-Based Sign Language Translation"
---

# SSL-SSAW: Self-Supervised Learning with Sigmoid Self-Attention Weighting for Question-Based Sign Language Translation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14036" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14036v1</a>
  <a href="https://arxiv.org/pdf/2509.14036.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14036v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14036v1', 'SSL-SSAW: Self-Supervised Learning with Sigmoid Self-Attention Weighting for Question-Based Sign Language Translation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zekang Liu, Wei Feng, Fanhua Shang, Lianyu Hu, Jichao Feng, Liqing Gao

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-17

---

## 💡 一句话要点

**提出基于问题的手语翻译任务及自监督学习融合方法SSL-SSAW**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `手语翻译` `自监督学习` `多模态融合` `对比学习` `注意力机制`

## 📋 核心要点

1. 现有手语翻译方法依赖词语标注，成本高昂且忽略了对话上下文。
2. 提出SSL-SSAW，利用对比学习对齐多模态特征，并用SSAW模块自适应提取特征。
3. 在CSL-Daily-QA和PHOENIX-2014T-QA数据集上达到SOTA，问题辅助效果优于词语辅助。

## 📝 摘要（中文）

本文提出了一种新的任务：基于问题的手语翻译（QB-SLT），旨在探索对话信息在手语翻译中的有效融合。与词语（手语转录）标注不同，对话自然存在于交流中，且更容易标注。该任务的关键挑战在于对齐多模态特征，同时利用问题的上下文来改进翻译。为了解决这个问题，我们提出了一种跨模态的自监督学习方法，结合Sigmoid自注意力权重（SSL-SSAW）进行手语翻译。具体来说，我们采用对比学习来对齐QB-SLT中的多模态特征，然后引入Sigmoid自注意力权重（SSAW）模块，用于从问题和手语序列中自适应地提取特征。此外，我们利用可用的问题文本，通过自监督学习来增强表征和翻译能力。我们在新建的CSL-Daily-QA和PHOENIX-2014T-QA数据集上评估了我们的方法，SSL-SSAW取得了SOTA性能。值得注意的是，易于获取的问题辅助可以达到甚至超过词语辅助的性能。此外，可视化结果表明，结合对话信息可以有效提高翻译质量。

## 🔬 方法详解

**问题定义**：现有手语翻译系统主要依赖于手语的词语（gloss）标注，这种标注方式成本高昂，且忽略了对话中重要的上下文信息。此外，如何有效地融合多模态信息，特别是问题文本和手语视频，是一个挑战。

**核心思路**：本文的核心思路是利用对话中的问题作为上下文信息，辅助手语翻译。通过自监督学习的方式，学习问题文本的表征，并将其与手语视频特征进行融合，从而提高翻译的准确性和流畅性。设计的SSAW模块能够自适应地学习问题和手语序列的权重，从而更好地提取相关特征。

**技术框架**：SSL-SSAW的整体框架包含以下几个主要模块：1) 特征提取模块：分别提取手语视频和问题文本的特征。2) 对比学习模块：利用对比学习对齐手语视频和问题文本的特征空间。3) SSAW模块：利用Sigmoid自注意力机制，自适应地学习问题和手语序列的权重，并进行特征融合。4) 翻译模块：将融合后的特征输入到翻译模型中，生成目标语言的句子。

**关键创新**：该论文的关键创新在于：1) 提出了基于问题的手语翻译任务（QB-SLT），更贴近实际应用场景。2) 提出了SSL-SSAW方法，通过对比学习和自注意力机制，有效地融合了多模态信息。3) 利用自监督学习增强了问题文本的表征能力。与现有方法相比，该方法不需要词语标注，且能够更好地利用对话上下文信息。

**关键设计**：对比学习模块使用了InfoNCE损失函数，用于拉近正样本（相关的手语视频和问题文本）之间的距离，推远负样本（不相关的手语视频和问题文本）之间的距离。SSAW模块使用了Sigmoid函数来生成权重，使得模型能够更加灵活地选择重要的特征。自监督学习模块使用了Masked Language Model (MLM) 目标，用于预测被mask掉的词语，从而增强问题文本的表征能力。

## 📊 实验亮点

SSL-SSAW在CSL-Daily-QA和PHOENIX-2014T-QA数据集上取得了SOTA性能。实验结果表明，利用问题辅助可以达到甚至超过词语辅助的性能，验证了该方法的有效性。可视化结果也表明，结合对话信息可以有效提高翻译质量。

## 🎯 应用场景

该研究成果可应用于智能手语翻译系统，帮助听障人士与健听人士进行无障碍交流。例如，在客服、教育、医疗等领域，可以利用该技术构建自动化的手语翻译服务，提高沟通效率和服务质量。未来，该技术还可以扩展到其他多模态翻译任务中，例如视频字幕生成、语音翻译等。

## 📄 摘要（原文）

> Sign Language Translation (SLT) bridges the communication gap between deaf people and hearing people, where dialogue provides crucial contextual cues to aid in translation. Building on this foundational concept, this paper proposes Question-based Sign Language Translation (QB-SLT), a novel task that explores the efficient integration of dialogue. Unlike gloss (sign language transcription) annotations, dialogue naturally occurs in communication and is easier to annotate. The key challenge lies in aligning multimodality features while leveraging the context of the question to improve translation. To address this issue, we propose a cross-modality Self-supervised Learning with Sigmoid Self-attention Weighting (SSL-SSAW) fusion method for sign language translation. Specifically, we employ contrastive learning to align multimodality features in QB-SLT, then introduce a Sigmoid Self-attention Weighting (SSAW) module for adaptive feature extraction from question and sign language sequences. Additionally, we leverage available question text through self-supervised learning to enhance representation and translation capabilities. We evaluated our approach on newly constructed CSL-Daily-QA and PHOENIX-2014T-QA datasets, where SSL-SSAW achieved SOTA performance. Notably, easily accessible question assistance can achieve or even surpass the performance of gloss assistance. Furthermore, visualization results demonstrate the effectiveness of incorporating dialogue in improving translation quality.

