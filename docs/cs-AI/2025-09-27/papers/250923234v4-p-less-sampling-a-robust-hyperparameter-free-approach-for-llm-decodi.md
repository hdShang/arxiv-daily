---
layout: default
title: "p-less Sampling: A Robust Hyperparameter-Free Approach for LLM Decoding"
---

# p-less Sampling: A Robust Hyperparameter-Free Approach for LLM Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23234" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23234v4</a>
  <a href="https://arxiv.org/pdf/2509.23234.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23234v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23234v4', 'p-less Sampling: A Robust Hyperparameter-Free Approach for LLM Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Runyan Tan, Shuang Wu, Phillip Howard

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-27 (更新: 2025-10-28)

**🔗 代码/项目**: [GITHUB](https://github.com/ryttry/p-less)

---

## 💡 一句话要点

**提出p-less采样方法，一种无需超参数的鲁棒LLM解码策略，提升生成质量。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM解码` `采样策略` `无超参数` `信息论` `文本生成`

## 📋 核心要点

1. 现有LLM解码采样方法依赖超参数调整，对不同任务和温度配置敏感，影响生成质量。
2. p-less采样基于信息论动态设置截断阈值，无需超参数，提升了采样方法的鲁棒性。
3. 实验表明，p-less采样在数学、推理和写作任务中优于现有方法，且在高温度下文本质量下降更少。

## 📝 摘要（中文）

从大型语言模型（LLM）获得高质量输出通常取决于基于采样的解码策略，该策略在每个生成步骤中概率性地选择下一个token。虽然已经提出了各种这样的采样方法，但它们的性能可能对超参数的选择很敏感，这可能需要根据生成任务和温度配置进行不同的设置。在这项工作中，我们介绍$p$-less采样：一种信息论的采样方法，它基于整个token概率分布在每个解码步骤动态设置截断阈值。与现有方法不同，$p$-less采样没有超参数，并且随着温度的升高，始终如一地产生高质量的输出。我们提供了关于$p$-less采样的理论视角，以支持我们提出的方法，并进行实验以实证验证其在数学、逻辑推理和创造性写作任务中的有效性。我们的结果表明，$p$-less采样始终优于现有的采样方法，同时在较高的温度值下文本质量的下降要小得多。我们进一步展示了$p$-less如何通过更低的平均token采样时间和更短的生成长度来实现比替代方法更高的推理时间效率，而又不牺牲准确性。最后，我们提供了分析，通过定性示例、案例研究和多样性评估来突出$p$-less的优势。代码可在https://github.com/ryttry/p-less 获取。

## 🔬 方法详解

**问题定义**：现有基于采样的LLM解码方法，如Top-k采样、Nucleus采样等，其性能高度依赖于超参数的选择。针对不同的生成任务和温度设置，需要手动调整这些超参数，过程繁琐且难以保证最佳性能。此外，在高温度设置下，这些方法容易产生低质量或不连贯的文本。

**核心思路**：p-less采样的核心思想是利用信息论原理，动态地确定一个截断阈值，该阈值基于整个token概率分布。这意味着在每个解码步骤，模型会自适应地选择一个概率较高的token子集，而不是像传统方法那样依赖固定的超参数。这种自适应性使得p-less采样能够更好地应对不同的任务和温度设置。

**技术框架**：p-less采样的整体流程如下：1. 获取LLM预测的token概率分布；2. 基于该分布，计算一个动态截断阈值；3. 仅从概率高于该阈值的token中进行采样；4. 将采样的token作为下一个输入，重复上述步骤直到生成结束。该方法不需要额外的训练或微调，可以直接应用于现有的LLM。

**关键创新**：p-less采样的关键创新在于其动态截断阈值的计算方式。与现有方法使用固定的超参数不同，p-less采样使用信息论原理，基于整个token概率分布自适应地确定阈值。这种方法能够更好地捕捉token之间的关系，并避免选择低概率的token，从而提高生成质量。

**关键设计**：p-less采样没有需要手动调整的超参数。其核心在于动态截断阈值的计算。具体而言，论文可能使用诸如熵、KL散度等信息论指标来衡量token概率分布的不确定性，并基于此确定截断阈值。具体的计算公式和实现细节需要在论文中进一步查找。

## 📊 实验亮点

实验结果表明，p-less采样在数学、逻辑推理和创造性写作任务中均优于现有的采样方法。尤其是在高温度设置下，p-less采样能够显著降低文本质量的下降。此外，p-less采样还实现了更高的推理效率，通过更低的平均token采样时间和更短的生成长度，在不牺牲准确性的前提下提升了性能。

## 🎯 应用场景

p-less采样可广泛应用于各种需要高质量文本生成的场景，如机器翻译、文本摘要、对话生成、代码生成等。其无需超参数的特性，降低了使用门槛，使得开发者可以更便捷地利用LLM生成高质量文本。该方法还有助于提升LLM在资源受限环境下的应用效率。

## 📄 摘要（原文）

> Obtaining high-quality outputs from Large Language Models (LLMs) often depends upon the choice of a sampling-based decoding strategy to probabilistically choose the next token at each generation step. While a variety of such sampling methods have been proposed, their performance can be sensitive to the selection of hyperparameters which may require different settings depending upon the generation task and temperature configuration. In this work, we introduce $p$-less sampling: an information-theoretic approach to sampling which dynamically sets a truncation threshold at each decoding step based on the entire token probability distribution. Unlike existing methods, $p$-less sampling has no hyperparameters and consistently produces high-quality outputs as temperature increases. We provide theoretical perspectives on $p$-less sampling to ground our proposed method and conduct experiments to empirically validate its effectiveness across a range of math, logical reasoning, and creative writing tasks. Our results demonstrate how $p$-less sampling consistently outperforms existing sampling approaches while exhibiting much less degradation in text quality at higher temperature values. We further show how $p$-less achieves greater inference-time efficiency than alternative methods through lower average token sampling times and shorter generation lengths, without sacrificing accuracy. Finally, we provide analyses to highlight the benefits of $p$-less through qualitative examples, case studies, and diversity assessments. The code is available at https://github.com/ryttry/p-less .

