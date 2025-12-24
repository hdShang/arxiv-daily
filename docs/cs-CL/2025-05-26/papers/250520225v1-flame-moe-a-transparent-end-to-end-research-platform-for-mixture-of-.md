---
layout: default
title: FLAME-MoE: A Transparent End-to-End Research Platform for Mixture-of-Experts Language Models
---

# FLAME-MoE: A Transparent End-to-End Research Platform for Mixture-of-Experts Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20225" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20225v1</a>
  <a href="https://arxiv.org/pdf/2505.20225.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20225v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20225v1', 'FLAME-MoE: A Transparent End-to-End Research Platform for Mixture-of-Experts Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Kang, Zichun Yu, Chenyan Xiong

**分类**: cs.CL, cs.LG

**发布日期**: 2025-05-26

**备注**: All code, training logs, and model checkpoints are available at https://github.com/cmu-flame/FLAME-MoE

**🔗 代码/项目**: [GITHUB](https://github.com/cmu-flame/FLAME-MoE)

---

## 💡 一句话要点

**提出FLAME-MoE以解决现有MoE语言模型研究平台不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家` `语言模型` `开源平台` `模型训练` `自然语言处理` `专家行为` `性能评估`

## 📋 核心要点

1. 现有的混合专家语言模型缺乏一个开放的研究平台，限制了学术界对其扩展性和路由行为的深入研究。
2. FLAME-MoE提供了一个开源的研究套件，包含多种规模的解码器模型，支持对MoE架构的全面实验和分析。
3. 在六个评估任务中，FLAME-MoE的平均准确率比相同FLOPs的稠密基线提高了最多3.4个百分点，显示出其有效性。

## 📝 摘要（中文）

近年来，像Gemini-1.5、DeepSeek-V3和Llama-4等大型语言模型越来越多地采用混合专家（MoE）架构，通过每个token仅激活模型的一部分来实现高效的性能权衡。然而，学术研究者仍缺乏一个完全开放的端到端MoE平台来研究扩展、路由和专家行为。为此，我们发布了FLAME-MoE，这是一个完全开源的研究套件，由七个仅解码器模型组成，活跃参数范围从3800万到17亿，其架构包含64个专家、前8个门控和2个共享专家，紧密反映现代生产LLM。所有训练数据管道、脚本、日志和检查点均可公开获取，以支持可重复的实验。在六个评估任务中，FLAME-MoE在与相同FLOPs训练的稠密基线相比，平均准确率提高了最多3.4个百分点。通过完全的训练跟踪透明性，我们展示了初步分析结果，表明专家在不同token子集上逐渐专业化，协同激活矩阵保持稀疏，反映出多样的专家使用情况，以及路由行为在训练早期即趋于稳定。所有代码、训练日志和模型检查点可在https://github.com/cmu-flame/FLAME-MoE获取。

## 🔬 方法详解

**问题定义**：论文旨在解决学术界缺乏开放的混合专家（MoE）语言模型研究平台的问题，现有方法在扩展性、路由和专家行为的研究上存在局限。

**核心思路**：FLAME-MoE通过提供一个完全开源的研究套件，包含多种规模的解码器模型，旨在支持对MoE架构的深入实验和分析，促进研究者对模型行为的理解。

**技术框架**：FLAME-MoE的整体架构包括七个解码器模型，活跃参数从3800万到17亿，采用64个专家、前8个门控和2个共享专家的设计，紧密反映现代生产LLM的架构。所有训练数据管道、脚本和日志均可公开获取。

**关键创新**：FLAME-MoE的主要创新在于其完全开源的特性和透明的训练跟踪，允许研究者对模型的扩展性和专家行为进行深入分析，这在现有的MoE研究中是前所未有的。

**关键设计**：FLAME-MoE的设计包括64个专家的配置、前8个门控机制和共享专家的设置，确保了模型在不同token子集上的专业化，同时保持协同激活矩阵的稀疏性，反映出多样的专家使用情况。

## 📊 实验亮点

FLAME-MoE在六个评估任务中表现出色，平均准确率比相同FLOPs的稠密基线提高了最多3.4个百分点，展示了其在效率与性能之间的优良平衡。此外，研究还揭示了专家在token子集上的专业化趋势和路由行为的稳定性。

## 🎯 应用场景

FLAME-MoE的研究成果可广泛应用于自然语言处理领域，尤其是在需要高效模型推理和训练的场景中，如对话系统、文本生成和机器翻译等。其开源特性将促进更多研究者参与到MoE架构的探索中，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Recent large language models such as Gemini-1.5, DeepSeek-V3, and Llama-4 increasingly adopt Mixture-of-Experts (MoE) architectures, which offer strong efficiency-performance trade-offs by activating only a fraction of the model per token. Yet academic researchers still lack a fully open, end-to-end MoE platform for investigating scaling, routing, and expert behavior. We release FLAME-MoE, a completely open-source research suite composed of seven decoder-only models, ranging from 38M to 1.7B active parameters, whose architecture--64 experts with top-8 gating and 2 shared experts--closely reflects modern production LLMs. All training data pipelines, scripts, logs, and checkpoints are publicly available to enable reproducible experimentation. Across six evaluation tasks, FLAME-MoE improves average accuracy by up to 3.4 points over dense baselines trained with identical FLOPs. Leveraging full training trace transparency, we present initial analyses showing that (i) experts increasingly specialize on distinct token subsets, (ii) co-activation matrices remain sparse, reflecting diverse expert usage, and (iii) routing behavior stabilizes early in training. All code, training logs, and model checkpoints are available at https://github.com/cmu-flame/FLAME-MoE.

