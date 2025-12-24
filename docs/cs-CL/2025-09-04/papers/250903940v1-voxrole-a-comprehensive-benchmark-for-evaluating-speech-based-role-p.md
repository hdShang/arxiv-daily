---
layout: default
title: "VoxRole: A Comprehensive Benchmark for Evaluating Speech-Based Role-Playing Agents"
---

# VoxRole: A Comprehensive Benchmark for Evaluating Speech-Based Role-Playing Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03940" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03940v1</a>
  <a href="https://arxiv.org/pdf/2509.03940.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03940v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03940v1', 'VoxRole: A Comprehensive Benchmark for Evaluating Speech-Based Role-Playing Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weihao Wu, Liang Cao, Xinyu Wu, Zhiwei Lin, Rui Niu, Jingbei Li, Zhiyong Wu

**分类**: cs.CL, cs.AI, cs.SD

**发布日期**: 2025-09-04

---

## 💡 一句话要点

**提出VoxRole：用于评估语音角色扮演代理的综合基准**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音角色扮演` `对话代理` `评估基准` `大型语言模型` `角色一致性`

## 📋 核心要点

1. 现有角色扮演对话代理研究主要集中于文本模态，忽略了语音中重要的超语言特征，限制了角色情感的表达。
2. 论文提出VoxRole基准，通过两阶段自动化流程，从电影中提取多轮对话和角色信息，构建了大规模语音角色扮演数据集。
3. 通过VoxRole对现有语音对话模型进行评估，揭示了模型在角色一致性方面的优缺点，为后续研究提供了重要参考。

## 📝 摘要（中文）

大型语言模型（LLMs）的显著进步极大地推动了角色扮演对话代理（RPCAs）的发展。这些系统旨在通过一致的角色扮演来创造沉浸式的用户体验。然而，当前RPCA研究面临双重局限性。首先，现有工作主要集中在文本模态，完全忽略了语音中关键的超语言特征，包括语调、韵律和节奏，这些特征对于传达角色情感和塑造生动身份至关重要。其次，基于语音的角色扮演领域长期缺乏标准化的评估基准。目前大多数口语对话数据集仅针对基本能力评估，角色设定简单或定义不清。因此，它们无法有效地量化模型在长期角色一致性等核心能力上的表现。为了解决这一关键差距，我们推出了VoxRole，这是第一个专门为评估基于语音的RPCAs而设计的综合基准。该基准包含13335个多轮对话，总计65.6小时的语音，来自261部电影中的1228个独特角色。为了构建这一资源，我们提出了一种新颖的两阶段自动化流程，该流程首先将电影音频与剧本对齐，然后使用LLM系统地构建每个角色的多维配置文件。利用VoxRole，我们对当代口语对话模型进行了多维度评估，揭示了它们在保持角色一致性方面的优势和局限性。

## 🔬 方法详解

**问题定义**：现有角色扮演对话代理的研究主要集中在文本模态，忽略了语音中的语调、韵律等超语言特征，导致角色情感表达不足。同时，缺乏专门针对语音角色扮演的评估基准，难以有效评估模型在长期角色一致性方面的表现。

**核心思路**：论文的核心思路是构建一个大规模、高质量的语音角色扮演数据集VoxRole，并利用该数据集对现有语音对话模型进行多维度评估。通过分析模型的表现，揭示其在角色一致性方面的优势和不足，从而为后续研究提供指导。

**技术框架**：VoxRole的构建包含两个主要阶段：1) 音频-剧本对齐：将电影音频与剧本进行对齐，提取对话片段。2) 角色信息构建：利用大型语言模型（LLM）分析剧本，为每个角色构建多维配置文件，包括性格、背景等信息。最终，将对齐的对话片段与角色信息进行整合，构建成VoxRole数据集。

**关键创新**：该论文的关键创新在于提出了一个自动化的两阶段流程，能够高效地从电影中提取高质量的语音角色扮演数据。此外，VoxRole是第一个专门针对语音角色扮演代理的综合评估基准，填补了该领域的空白。

**关键设计**：在音频-剧本对齐阶段，采用了强制对齐技术，确保对话片段的准确性。在角色信息构建阶段，利用LLM进行知识抽取和推理，生成角色的多维配置文件。数据集包含13335个多轮对话，总计65.6小时的语音，来自261部电影中的1228个独特角色。

## 📊 实验亮点

论文利用VoxRole基准对现有语音对话模型进行了评估，结果表明，现有模型在角色一致性方面仍存在较大提升空间。通过对不同模型的表现进行分析，论文揭示了模型在处理不同角色类型、对话长度等方面的优缺点，为后续模型改进提供了重要参考。

## 🎯 应用场景

VoxRole基准的提出，为语音角色扮演代理的研究提供了重要的资源和评估工具。该基准可以用于训练和评估各种语音对话模型，提升模型在角色一致性、情感表达等方面的能力。未来，该研究可以应用于智能客服、虚拟助手、游戏角色等领域，创造更加沉浸式和个性化的用户体验。

## 📄 摘要（原文）

> Recent significant advancements in Large Language Models (LLMs) have greatly propelled the development of Role-Playing Conversational Agents (RPCAs). These systems aim to create immersive user experiences through consistent persona adoption. However, current RPCA research faces dual limitations. First, existing work predominantly focuses on the textual modality, entirely overlooking critical paralinguistic features including intonation, prosody, and rhythm in speech, which are essential for conveying character emotions and shaping vivid identities. Second, the speech-based role-playing domain suffers from a long-standing lack of standardized evaluation benchmarks. Most current spoken dialogue datasets target only fundamental capability assessments, featuring thinly sketched or ill-defined character profiles. Consequently, they fail to effectively quantify model performance on core competencies like long-term persona consistency. To address this critical gap, we introduce VoxRole, the first comprehensive benchmark specifically designed for the evaluation of speech-based RPCAs. The benchmark comprises 13335 multi-turn dialogues, totaling 65.6 hours of speech from 1228 unique characters across 261 movies. To construct this resource, we propose a novel two-stage automated pipeline that first aligns movie audio with scripts and subsequently employs an LLM to systematically build multi-dimensional profiles for each character. Leveraging VoxRole, we conduct a multi-dimensional evaluation of contemporary spoken dialogue models, revealing crucial insights into their respective strengths and limitations in maintaining persona consistency.

