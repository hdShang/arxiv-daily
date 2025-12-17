---
layout: default
title: Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning
---

# Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.11027" target="_blank" class="toolbar-btn">arXiv: 2510.11027v1</a>
    <a href="https://arxiv.org/pdf/2510.11027.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11027v1" 
            onclick="toggleFavorite(this, '2510.11027v1', 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Ganlin Yang, Tianyi Zhang, Haoran Hao, Weiyun Wang, Yibin Liu, Dehui Wang, Guanzhou Chen, Zijian Cai, Junting Chen, Weijie Su, Wengang Zhou, Yu Qiao, Jifeng Dai, Jiangmiao Pang, Gen Luo, Wenhai Wang, Yao Mu, Zhi Hou

**分类**: cs.CV

**发布日期**: 2025-10-13

---

## 💡 一句话要点

**Vlaser：提出具有协同具身推理能力的视觉-语言-动作模型，弥合VLM推理与VLA策略学习的鸿沟。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `具身推理` `机器人控制` `策略学习` `领域自适应`

## 📋 核心要点

1. 现有方法未能有效衔接上游VLM推理与下游VLA策略学习，限制了端到端机器人控制的性能。
2. Vlaser模型通过整合高层推理和底层控制，旨在弥合VLM推理与VLA策略学习之间的差距。
3. Vlaser在多个具身推理任务上取得了SOTA性能，并在机器人控制基准测试中表现出竞争力。

## 📝 摘要（中文）

本文旨在弥合基于视觉-语言模型(VLM)的推理与视觉-语言-动作(VLA)策略学习之间的关键差距。为此，我们提出了Vlaser，一个具有协同具身推理能力的视觉-语言-动作模型。Vlaser是一个基础视觉-语言模型，旨在将高层推理与具身智能体的底层控制相结合。基于高质量的Vlaser-6M数据集，Vlaser在一系列具身推理基准测试中实现了最先进的性能，包括空间推理、具身定位、具身问答和任务规划。此外，我们系统地研究了不同的VLM初始化如何影响监督VLA微调，为减轻互联网规模预训练数据与特定于具身策略学习数据之间的领域转移提供了新的见解。基于这些见解，我们的方法在WidowX基准测试上取得了最先进的结果，并在Google Robot基准测试上取得了具有竞争力的性能。

## 🔬 方法详解

**问题定义**：现有VLA模型通常依赖于独立的VLM进行推理，然后将推理结果传递给策略学习模块。这种分离导致信息损失和次优的端到端性能。此外，互联网规模的预训练数据与具身环境下的策略学习数据存在显著的领域差异，进一步加剧了这一问题。

**核心思路**：Vlaser的核心思路是将高层推理和底层控制集成到一个统一的视觉-语言-动作模型中。通过联合训练，Vlaser能够更好地理解具身环境，并生成更有效的动作策略。此外，论文还研究了不同的VLM初始化策略，以减轻领域差异带来的影响。

**技术框架**：Vlaser的整体架构包含视觉编码器、语言编码器、动作解码器以及一个用于融合视觉和语言信息的跨模态交互模块。视觉编码器负责提取图像特征，语言编码器负责处理文本指令，跨模态交互模块将视觉和语言信息融合，最后动作解码器生成相应的动作指令。整个模型采用端到端的方式进行训练。

**关键创新**：Vlaser的关键创新在于其协同具身推理能力，即模型能够同时进行高层推理和底层控制，从而实现更有效的具身智能体行为。此外，对VLM初始化策略的研究也为缓解领域差异提供了新的思路。

**关键设计**：Vlaser使用了Transformer架构作为其核心构建块，并采用了对比学习损失来增强视觉和语言表示之间的对齐。此外，论文还探索了不同的VLM初始化策略，包括直接使用预训练的VLM权重、对预训练的VLM进行微调以及从头开始训练VLM。

## 📊 实验亮点

Vlaser在空间推理、具身定位、具身问答和任务规划等多个具身推理基准测试中取得了最先进的性能。此外，在WidowX机器人控制基准测试上，Vlaser也取得了SOTA结果，并在Google Robot基准测试上表现出竞争力。这些结果表明Vlaser在具身智能体领域具有显著的优势。

## 🎯 应用场景

Vlaser模型可应用于各种机器人控制任务，例如家庭服务机器人、工业自动化机器人和搜索救援机器人。通过将高层推理与底层控制相结合，Vlaser能够使机器人更好地理解人类指令，并在复杂环境中执行任务。该研究的未来影响包括提高机器人的自主性和智能化水平，使其能够更好地服务于人类。

## 📄 摘要（原文）

> While significant research has focused on developing embodied reasoning capabilities using Vision-Language Models (VLMs) or integrating advanced VLMs into Vision-Language-Action (VLA) models for end-to-end robot control, few studies directly address the critical gap between upstream VLM-based reasoning and downstream VLA policy learning. In this work, we take an initial step toward bridging embodied reasoning with VLA policy learning by introducing Vlaser - a Vision-Language-Action Model with synergistic embodied reasoning capability, which is a foundational vision-language model designed to integrate high-level reasoning with low-level control for embodied agents. Built upon the high-quality Vlaser-6M dataset, Vlaser achieves state-of-the-art performance across a range of embodied reasoning benchmarks - including spatial reasoning, embodied grounding, embodied QA, and task planning. Furthermore, we systematically examine how different VLM initializations affect supervised VLA fine-tuning, offering novel insights into mitigating the domain shift between internet-scale pre-training data and embodied-specific policy learning data. Based on these insights, our approach achieves state-of-the-art results on the WidowX benchmark and competitive performance on the Google Robot benchmark.

