---
layout: default
title: "LD-MoLE: Learnable Dynamic Routing for Mixture of LoRA Experts"
---

# LD-MoLE: Learnable Dynamic Routing for Mixture of LoRA Experts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25684" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25684v1</a>
  <a href="https://arxiv.org/pdf/2509.25684.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25684v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25684v1', 'LD-MoLE: Learnable Dynamic Routing for Mixture of LoRA Experts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuan Zhuang, Yi Shen, Yuexin Bian, Qing Su, Shihao Ji, Yuanyuan Shi, Fei Miao

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出LD-MoLE，通过可学习动态路由实现LoRA专家混合，提升LLM微调性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `参数高效微调` `混合专家模型` `动态路由` `可学习路由`

## 📋 核心要点

1. 现有MoE方法依赖TopK路由，超参数敏感且专家分配固定，限制了模型性能。
2. LD-MoLE采用可学习动态路由，通过可微分函数和闭式解实现自适应专家分配。
3. 实验表明，LD-MoLE在多个基准测试中超越SOTA方法，并能学习token和层级的专家分配。

## 📝 摘要（中文）

本文提出了一种名为LD-MoLE的可学习动态路由机制，用于LoRA专家混合，旨在提升大型语言模型（LLM）在下游任务上的适应能力。现有方法通常依赖于TopK路由，需要精细的超参数调整，并且为每个token分配固定数量的专家。LD-MoLE通过可微分的路由函数和闭式解取代了不可微的TopK选择，实现了自适应的、token相关的、以及层级的专家分配。此外，该方法允许模型自适应地确定在不同层为每个token激活的专家数量。同时，引入了解析稀疏性控制目标来正则化激活专家的数量。在Qwen3-1.7B和Llama-3.2-3B模型上的大量实验表明，LD-MoLE在各种基准测试中取得了优于现有最佳方法的平均分数。该方法不仅实现了卓越的性能，还展示了学习token相关和层级专家分配的能力。

## 🔬 方法详解

**问题定义**：现有基于MoE的LLM微调方法，特别是结合LoRA的方法，通常使用TopK路由机制。这种机制存在两个主要问题：一是需要手动调整TopK中的K值，对超参数非常敏感；二是每个token被分配的专家数量是固定的，无法根据token的特性进行自适应调整，限制了模型的表达能力和效率。

**核心思路**：LD-MoLE的核心思路是使用一个可学习的动态路由机制来替代传统的TopK路由。通过引入可微分的路由函数，模型可以根据token的特征自适应地选择激活的专家，并且可以动态地调整每个token激活的专家数量。这种自适应性使得模型能够更好地捕捉token之间的差异，从而提高性能。

**技术框架**：LD-MoLE的技术框架主要包括以下几个模块：1) LoRA专家层：使用多个LoRA模块作为专家，每个专家负责处理不同类型的token；2) 可学习路由函数：使用一个神经网络来预测每个token应该激活哪些专家，以及激活的权重；3) 闭式解：使用闭式解来计算每个专家的激活概率，从而避免了使用采样等近似方法；4) 稀疏性控制：引入一个稀疏性控制目标来正则化激活专家的数量，避免模型过度依赖少数专家。

**关键创新**：LD-MoLE最重要的技术创新点在于其可学习的动态路由机制。与传统的TopK路由相比，LD-MoLE可以根据token的特征自适应地选择激活的专家，并且可以动态地调整每个token激活的专家数量。此外，LD-MoLE还引入了一个闭式解来计算每个专家的激活概率，避免了使用采样等近似方法，提高了模型的训练效率和稳定性。

**关键设计**：LD-MoLE的关键设计包括：1) 使用softmax函数作为可微分的路由函数，使得模型可以预测每个token应该激活哪些专家，以及激活的权重；2) 引入KL散度作为稀疏性控制目标，鼓励模型激活尽可能少的专家；3) 使用闭式解来计算每个专家的激活概率，避免了使用采样等近似方法；4) 在不同的层使用不同的路由函数，使得模型可以学习到层级的专家分配。

## 📊 实验亮点

实验结果表明，LD-MoLE在Qwen3-1.7B和Llama-3.2-3B模型上，相比于SOTA基线方法，在多个基准测试中取得了最高的平均分数。这证明了LD-MoLE能够有效地学习token相关和层级的专家分配，从而提升模型的性能。具体性能提升数据在论文中有详细展示。

## 🎯 应用场景

LD-MoLE具有广泛的应用前景，可用于各种需要对大型语言模型进行高效微调的场景，例如自然语言处理、机器翻译、文本生成等。该方法能够提升模型在特定任务上的性能，并降低计算成本，尤其适用于资源受限的环境。未来，LD-MoLE有望应用于更复杂的模型结构和更大规模的数据集，进一步提升LLM的适应性和泛化能力。

## 📄 摘要（原文）

> Recent studies have shown that combining parameter-efficient fine-tuning (PEFT) with mixture-of-experts (MoE) is an effective strategy for adapting large language models (LLMs) to the downstream tasks. However, most existing approaches rely on conventional TopK routing, which requires careful hyperparameter tuning and assigns a fixed number of experts to each token. In this work, we propose LD-MoLE, a Learnable Dynamic routing mechanism for Mixture of LoRA Experts that enables adaptive, token-dependent, and layer-wise expert allocation. Our method replaces the non-differentiable TopK selection with a differentiable routing function and a closed-form solution. Moreover, our design allows the model to adaptively determine the number of experts to activate for each token at different layers. In addition, we introduce an analytical sparsity control objective to regularize the number of activated experts. Extensive experiments on the Qwen3-1.7B and Llama-3.2-3B models show that LD-MoLE achieves the highest average scores compared to state-of-the-art baselines, across a diverse set of benchmarks. Our method not only achieves superior performance, but also demonstrates the ability to learn token-dependent and layer-wise expert allocation.

