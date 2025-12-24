---
layout: default
title: "SignBind-LLM: Multi-Stage Modality Fusion for Sign Language Translation"
---

# SignBind-LLM: Multi-Stage Modality Fusion for Sign Language Translation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00030" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00030v3</a>
  <a href="https://arxiv.org/pdf/2509.00030.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00030v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00030v3', 'SignBind-LLM: Multi-Stage Modality Fusion for Sign Language Translation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marshall Thomas, Edward Fish, Richard Bowden

**分类**: cs.CL, cs.CV

**发布日期**: 2025-08-20 (更新: 2025-12-04)

---

## 💡 一句话要点

**提出SignBind-LLM以解决手语翻译中的多模态融合问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `手语翻译` `多模态融合` `大型语言模型` `模块化框架` `拼写识别` `唇读识别` `时间对齐`

## 📋 核心要点

1. 现有的手语翻译方法在快速拼写和面部非手动线索的识别上存在显著不足，导致翻译效果不佳。
2. 论文提出的SignBind-LLM框架通过模块化设计，分别处理不同的手语成分，从而提高翻译的准确性。
3. 实验结果显示，该方法在多个数据集上取得了显著提升，BLEU-4分数和字母准确率均创下新高。

## 📝 摘要（中文）

尽管在无注释手语翻译（SLT）方面取得了一定进展，传统的单模态端到端方法在自然手语的两个关键组成部分上仍然存在不足：快速拼写的精确识别和面部非手动线索的异步整合。最近，利用大型语言模型的SLT进展虽然规避了这一挑战，但迫使单一网络同时学习这些任务，导致在翻译姓名、地点和技术术语等关键信息时表现不佳。为此，我们提出了SignBind-LLM，一个模块化框架，旨在克服这些局限。该方法为连续手语、拼写和唇读分别设计了专门的预测器，通过轻量级变换器融合这些并行流，最终将组合表示传递给大型语言模型进行句子生成。我们的研究在How2Sign、ChicagoFSWildPlus和BOBSL数据集上建立了新的最先进水平，验证了我们核心假设的有效性。

## 🔬 方法详解

**问题定义**：本论文旨在解决手语翻译中的多模态融合问题，现有方法在快速拼写和面部非手动线索的识别上表现不佳，导致翻译效果不理想。

**核心思路**：我们提出的SignBind-LLM框架采用模块化设计，分别为连续手语、拼写和唇读构建专门的预测器，以便在融合前独立解决各个识别任务。

**技术框架**：整体架构包括三个主要模块：连续手语预测器、拼写预测器和唇读预测器。每个模块将其特定模态解码为一系列标记，随后通过轻量级变换器融合这些并行流，最后将组合表示传递给大型语言模型进行句子生成。

**关键创新**：本研究的核心创新在于将不同的识别任务分开处理，避免了单一网络同时学习多个任务的弊端，从而提高了翻译的准确性和鲁棒性。

**关键设计**：在设计中，我们采用了轻量级变换器以解决时间对齐问题，并在每个预测器中使用了特定的损失函数和网络结构，以确保各个模态的高效学习和融合。

## 📊 实验亮点

实验结果表明，SignBind-LLM在How2Sign数据集上达到了BLEU-4分数22.1，在ChicagoFSWildPlus数据集上实现了73.2%的字母准确率，在BOBSL数据集上获得了BLEU-4分数6.8，均创下了新的最先进水平，验证了我们的方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括手语翻译系统、教育工具以及辅助沟通设备，能够帮助听障人士更好地与社会互动。未来，该框架有望在多模态学习和人机交互等领域产生更广泛的影响。

## 📄 摘要（原文）

> Despite progress in gloss-free Sign Language Translation (SLT), traditional single modality end-to-end approaches consistently fail on two critical components of natural signing: the precise recognition of high-speed fingerspelling and the integration of asynchronous non-manual cues from the face. Recent progress in SLT with Large Language Models has side stepped this challenge, forcing a single network to learn these simultaneously resulting in poor performance when tasked with translating crucial information such as names, places, and technical terms. We introduce SignBind-LLM, a modular framework designed to overcome these limitations. Our approach employs separate, specialized predictors for continuous signing, fingerspelling, and lipreading. Each expert network first decodes its specific modality into a sequence of tokens. These parallel streams are then fused by a lightweight transformer that resolves temporal misalignments before passing the combined representation to a Large Language Model (LLM) for final sentence generation. Our method establishes a new state-of-the-art on the How2Sign, ChicagoFSWildPlus, and BOBSL datasets with a BLEU-4 score of 22.1, 73.2% letter accuracy and BLEU-4 score of 6.8 respectively. These results validate our core hypothesis: isolating and solving distinct recognition tasks before fusion provides a more powerful and effective pathway to robust, high-fidelity sign language translation.

