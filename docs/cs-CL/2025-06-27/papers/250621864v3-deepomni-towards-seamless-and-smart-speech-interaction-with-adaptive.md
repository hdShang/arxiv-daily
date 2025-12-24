---
layout: default
title: "DeepOmni: Towards Seamless and Smart Speech Interaction with Adaptive Modality-Specific MoE"
---

# DeepOmni: Towards Seamless and Smart Speech Interaction with Adaptive Modality-Specific MoE

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21864" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21864v3</a>
  <a href="https://arxiv.org/pdf/2506.21864.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21864v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21864v3', 'DeepOmni: Towards Seamless and Smart Speech Interaction with Adaptive Modality-Specific MoE')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hang Shao, Heting Gao, Yunhang Shen, Jiawei Chen, Zuwei Long, Dong Yang, Ke Li, Xing Sun

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-27 (更新: 2025-10-27)

**备注**: Under Review

**🔗 代码/项目**: [GITHUB](https://github.com/talkking/DeepTalk)

---

## 💡 一句话要点

**提出DeepTalk以解决多模态大语言模型的遗忘与性能下降问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `混合专家` `自适应学习` `语音交互` `灾难性遗忘` `性能优化` `智能助手`

## 📋 核心要点

1. 现有的原生多模态大语言模型在训练时面临灾难性遗忘和性能下降，尤其是配对语音-文本数据不足的问题。
2. DeepTalk框架通过混合专家架构实现自适应模态专家学习，动态区分模态专家并进行专门的单模态训练和联合多模态训练。
3. 实验结果显示，DeepTalk在性能上仅下降5.5%，远低于原生MLLMs的平均20%下降，同时对话延迟保持在0.5秒以内。

## 📝 摘要（中文）

本论文提出了一种名为DeepTalk的框架，旨在解决现有原生多模态大语言模型（MLLMs）在训练过程中面临的灾难性遗忘和性能下降问题。与传统的模块化MLLMs相比，DeepTalk通过混合专家（MoE）架构实现了自适应的模态专家学习，能够根据模态负载动态区分专家，并进行单模态和多模态的联合训练。实验结果表明，DeepTalk在性能上仅较原始大语言模型下降5.5%，显著低于原生MLLMs通常超过20%的性能下降，同时保持了0.5秒以内的对话延迟，确保了流畅的语音交互体验。

## 🔬 方法详解

**问题定义**：本论文旨在解决原生多模态大语言模型在训练过程中由于配对语音-文本数据不足而导致的灾难性遗忘和性能下降问题。现有方法在面对丰富的文本数据时，难以有效利用有限的语音数据进行预训练，导致模型性能不稳定。

**核心思路**：论文提出的DeepTalk框架通过混合专家（MoE）架构，动态区分模态专家，针对不同模态进行专门的训练，从而提高模型在多模态任务中的表现和稳定性。这样的设计使得模型能够更好地适应不同的输入模态，减少遗忘现象。

**技术框架**：DeepTalk的整体架构包括两个主要阶段：首先是自适应模态专家的区分和单模态训练，其次是联合多模态协同训练。每个模态专家根据其模态负载进行训练，确保在多模态环境下的有效学习。

**关键创新**：DeepTalk的核心创新在于其自适应模态专家学习机制，通过动态调整模态专家的训练策略，显著降低了性能下降幅度。这一机制与传统的模块化MLLMs相比，提供了更高的灵活性和适应性。

**关键设计**：在技术细节上，DeepTalk采用了特定的损失函数来平衡不同模态的训练，同时在网络结构上引入了混合专家机制，以便在多模态输入时能够有效选择合适的专家进行处理。

## 📊 实验亮点

DeepTalk在实验中表现出色，性能下降仅为5.5%，显著低于原生多模态大语言模型通常超过20%的下降幅度。此外，模型的对话延迟保持在0.5秒以内，确保了用户体验的流畅性。

## 🎯 应用场景

该研究的潜在应用领域包括智能语音助手、在线客服系统以及人机交互界面等。通过提升多模态交互的流畅性和智能性，DeepTalk能够为用户提供更自然的交流体验，推动语音技术的进一步发展与普及。

## 📄 摘要（原文）

> Native multimodal large language models (MLLMs) restructure a single large language model (LLM) into a spoken language model (SLM) capable of both speech and text generation. Compared to modular and aligned MLLMs, native MLLMs preserve richer paralinguistic features such as emotion and prosody, and generate speech responses directly within the backbone LLM rather than using a separate speech decoder. This integration also results in lower response latency and smoother interaction. However, native MLLMs suffer from catastrophic forgetting and performance degradation because the available paired speech-text data is insufficient to support the pretraining of MLLMs compared to the vast amount of text data required to pretrain text LLMs. To address this issue, we propose DeepTalk, a framework for adaptive modality expert learning based on a Mixture of Experts (MoE) architecture. DeepTalk first adaptively distinguishes modality experts according to their modality load within the LLM. Each modality expert then undergoes specialized single-modality training, followed by joint multimodal collaborative training. As a result, DeepTalk incurs only a 5.5% performance drop compared to the original LLM, which is significantly lower than the average performance drop of over 20% typically seen in native MLLMs (such as GLM-4-Voice), and is on par with modular MLLMs. Meanwhile, the end-to-end dialogue latency remains within 0.5 seconds, ensuring a seamless and intelligent speech interaction experience. Code and models are released at https://github.com/talkking/DeepTalk.

