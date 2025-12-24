---
layout: default
title: "AudioRole: An Audio Dataset for Character Role-Playing in Large Language Models"
---

# AudioRole: An Audio Dataset for Character Role-Playing in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23435" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23435v1</a>
  <a href="https://arxiv.org/pdf/2509.23435.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23435v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23435v1', 'AudioRole: An Audio Dataset for Character Role-Playing in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenyu Li, Xiaoqi Jiao, Yi Chang, Guangyan Zhang, Yiwen Guo

**分类**: cs.SD, cs.AI, cs.MM, eess.AS

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**提出AudioRole数据集，提升大语言模型在角色扮演中的音频个性化能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音频角色扮演` `大型语言模型` `数据集` `语音个性化` `多模态学习`

## 📋 核心要点

1. 现有角色扮演大语言模型主要集中于文本，缺乏对音频特征的同步建模，导致音频角色扮演效果不佳。
2. AudioRole数据集通过提供大规模、高质量的同步音频-文本数据，以及说话人身份和上下文信息，弥补了这一不足。
3. 实验表明，基于AudioRole训练的模型在声学和内容个性化方面均优于现有模型，验证了数据集的有效性。

## 📝 摘要（中文）

为了提升大型语言模型（LLMs）的角色扮演能力，尤其是在音频角色扮演（ARP）方面，本文提出了AudioRole数据集。该数据集从13个电视剧中精选了超过1000小时的音频，包含100万+个基于角色的对话，并提供了同步的音频-文本对，以及说话人身份和上下文元数据标注。为了验证数据集的有效性，作者还提出了ARP-Eval，一个双重评估框架，用于评估回复质量和角色保真度。实验结果表明，基于AudioRole训练的GLM-4-Voice模型（称为ARP-Model）在声学个性化方面取得了显著提升，平均声学个性化得分达到0.31，优于原始GLM-4-voice和更强大的MiniCPM-O-2.6模型。在内容个性化方面，ARP-Model的得分也达到了0.36，比未经训练的原始模型提高了约38%，并与MiniCPM-O-2.6模型持平。AudioRole包含超过115个主要角色的对话，6个训练好的ARP-Model，以及评估协议，为推进音频角色扮演研究提供了重要资源。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在角色扮演任务中，主要关注文本信息，忽略了语音中的声学特征，导致在音频角色扮演场景下，无法准确模拟角色的声音特点和情感表达。现有方法缺乏高质量的、包含同步音频-文本对以及说话人信息的训练数据，难以提升模型在音频角色扮演方面的性能。

**核心思路**：本文的核心思路是构建一个大规模、高质量的音频角色扮演数据集AudioRole，该数据集包含丰富的角色对话音频和对应的文本，并标注了说话人身份和上下文信息。通过在该数据集上训练大型语言模型，可以使模型学习到角色声音的个性化特征，从而提升其在音频角色扮演任务中的表现。

**技术框架**：AudioRole数据集的构建流程主要包括以下几个步骤：1) 数据收集：从13个电视剧中收集音频和文本数据。2) 数据清洗：对收集到的数据进行清洗和过滤，去除噪声和错误信息。3) 数据标注：对清洗后的数据进行标注，包括说话人身份、对话内容和上下文信息。4) 数据划分：将标注后的数据划分为训练集、验证集和测试集。此外，论文还提出了ARP-Eval评估框架，用于评估模型的回复质量和角色保真度。

**关键创新**：该论文的关键创新在于构建了一个大规模、高质量的音频角色扮演数据集AudioRole，该数据集包含了丰富的角色对话音频和对应的文本，并标注了说话人身份和上下文信息。这是首个专门为音频角色扮演任务设计的数据集，为该领域的研究提供了重要资源。

**关键设计**：AudioRole数据集包含超过1000小时的音频，100万+个基于角色的对话，以及超过115个主要角色。数据集中的音频和文本数据是同步的，并且标注了说话人身份和上下文信息。ARP-Eval评估框架包含声学个性化和内容个性化两个方面，用于全面评估模型的性能。

## 📊 实验亮点

实验结果表明，基于AudioRole训练的ARP-Model在声学个性化方面取得了显著提升，平均声学个性化得分达到0.31，优于原始GLM-4-voice和更强大的MiniCPM-O-2.6模型。在内容个性化方面，ARP-Model的得分也达到了0.36，比未经训练的原始模型提高了约38%，并与MiniCPM-O-2.6模型持平。

## 🎯 应用场景

该研究成果可应用于智能客服、虚拟助手、游戏角色扮演等领域。通过使用AudioRole数据集训练的模型，可以创建更具个性化和真实感的语音交互体验，提升用户满意度和沉浸感。未来，该数据集还可以用于研究语音情感识别、说话人识别等相关任务。

## 📄 摘要（原文）

> The creation of high-quality multimodal datasets remains fundamental for advancing role-playing capabilities in large language models (LLMs). While existing works predominantly focus on text-based persona simulation, Audio Role-Playing (ARP) presents unique challenges due to the need for synchronized alignment of semantic content and vocal characteristics. To address this gap, we propose AudioRole, a meticulously curated dataset from 13 TV series spanning 1K+ hours with 1M+ character-grounded dialogues, providing synchronized audio-text pairs annotated with speaker identities and contextual metadata. In addition, to demonstrate the effectiveness of the dataset, we introduced ARP-Eval, a dual-aspect evaluation framework that assesses both response quality and role fidelity. Empirical validation showing GLM-4-Voice trained on AudioRole (which we called ARP-Model) achieve an average Acoustic Personalization score of 0.31, significantly outperforming the original GLM-4-voice and the more powerful model MiniCPM-O-2.6, which specifically supports role-playing in one-shot scenarios. The ARP-Model also achieves a Content Personalization score of 0.36, surpassing the untrained original model by about 38% and maintaining the same level as MiniCPM-O-2.6.
>   AudioRole features dialogues from over 115 main characters, 6 trained ARP-Models that role-play different characters, and evaluation protocols. Together, they provide an essential resource for advancing audio-grounded role-playing research.

