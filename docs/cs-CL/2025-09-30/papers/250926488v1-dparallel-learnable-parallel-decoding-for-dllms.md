---
layout: default
title: "dParallel: Learnable Parallel Decoding for dLLMs"
---

# dParallel: Learnable Parallel Decoding for dLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26488" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26488v1</a>
  <a href="https://arxiv.org/pdf/2509.26488.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26488v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26488v1', 'dParallel: Learnable Parallel Decoding for dLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zigeng Chen, Gongfan Fang, Xinyin Ma, Ruonan Yu, Xinchao Wang

**分类**: cs.CL

**发布日期**: 2025-09-30

**备注**: Working in progress, code base: https://github.com/czg1225/dParallel

**🔗 代码/项目**: [GITHUB](https://github.com/czg1225/dParallel)

---

## 💡 一句话要点

**dParallel：面向扩散语言大模型的并行可学习解码方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散语言模型` `并行解码` `知识蒸馏` `确定性强制` `推理加速` `自然语言生成` `大语言模型`

## 📋 核心要点

1. 现有扩散语言模型(dLLMs)的并行解码潜力未被充分挖掘，推理效率提升受限，需要减少解码步骤。
2. dParallel通过确定性强制蒸馏，加速masked tokens的确定性收敛，从而实现更高效的并行解码。
3. 实验表明，dParallel在GSM8K和MBPP等基准测试中，显著减少解码步骤，实现高达10.5倍的加速，同时保持模型性能。

## 📝 摘要（中文）

扩散语言大模型(dLLMs)作为自回归生成的一种有前景的替代方案，因其并行token预测和更低的推理延迟而备受研究界关注。然而，它们的并行解码潜力在很大程度上仍未被充分探索，因为现有的开源模型仍然需要接近token长度的解码步骤才能确保性能。为了解决这个问题，我们提出了dParallel，一种简单有效的方法，可以释放dLLMs的固有并行性以实现快速采样。我们发现并行解码的关键瓶颈来自于masked tokens的顺序确定性收敛。基于这一洞察，我们引入了我们方法的核心：确定性强制蒸馏，这是一种新颖的训练策略，它蒸馏模型以遵循其原始采样轨迹，同时强制它更快、更并行地在masked tokens上实现高确定性。在各种基准上的大量实验表明，我们的方法可以显著减少解码步骤的数量，同时保持性能。当应用于LLaDA-8B-Instruct模型时，dParallel将GSM8K上的解码步骤从256减少到30，实现了8.5倍的加速而没有性能下降。在MBPP基准上，它将解码步骤从256减少到24，从而在保持准确性的同时实现了10.5倍的加速。我们的代码可在https://github.com/czg1225/dParallel 获得。

## 🔬 方法详解

**问题定义**：论文旨在解决扩散语言模型(dLLMs)并行解码效率低下的问题。现有dLLMs虽然理论上支持并行生成token，但实际应用中仍需大量的解码步骤，限制了推理速度。这是因为masked tokens的确定性收敛是顺序进行的，导致无法充分利用并行计算的优势。

**核心思路**：论文的核心思路是通过训练策略，使模型能够更快地对masked tokens产生高置信度的预测，从而减少所需的解码步骤。具体而言，通过“确定性强制蒸馏”方法，让模型学习在更少的步骤内达到与原始模型相似的预测结果。

**技术框架**：dParallel的技术框架主要包含两个阶段：首先，使用原始的dLLM进行采样，得到token生成轨迹。然后，使用“确定性强制蒸馏”方法训练新的模型，使其模仿原始模型的生成轨迹，并在更少的步骤内达到高置信度。这个过程可以看作是知识蒸馏的一种形式，其中原始模型是教师模型，新的模型是学生模型。

**关键创新**：该论文的关键创新在于提出了“确定性强制蒸馏”这一训练策略。与传统的知识蒸馏不同，该方法不仅关注最终的预测结果，还关注中间的生成轨迹，从而保证了在减少解码步骤的同时，模型的性能不会下降。此外，该方法还强制模型更快地对masked tokens产生高置信度的预测，从而加速了并行解码的过程。

**关键设计**：在“确定性强制蒸馏”中，损失函数的设计至关重要。论文可能采用了多种损失函数的组合，例如：1) 模仿损失，用于衡量学生模型与教师模型生成轨迹的相似度；2) 确定性损失，用于鼓励学生模型更快地对masked tokens产生高置信度的预测；3) 标准的语言模型损失，用于保持模型的语言建模能力。具体的参数设置和网络结构细节需要在论文原文中查找。

## 📊 实验亮点

dParallel在LLaDA-8B-Instruct模型上进行了实验，结果表明，在GSM8K基准测试中，解码步骤从256减少到30，实现了8.5倍的加速，而性能没有下降。在MBPP基准测试中，解码步骤从256减少到24，实现了10.5倍的加速，同时保持了准确性。这些结果表明，dParallel能够显著提高dLLMs的推理效率。

## 🎯 应用场景

dParallel具有广泛的应用前景，可用于加速各种基于扩散模型的自然语言生成任务，例如文本摘要、机器翻译、代码生成等。通过减少推理延迟，dParallel可以提升用户体验，并降低部署成本，尤其是在对延迟敏感的应用场景中，例如在线对话系统和实时内容生成。

## 📄 摘要（原文）

> Diffusion large language models (dLLMs) have recently drawn considerable attention within the research community as a promising alternative to autoregressive generation, offering parallel token prediction and lower inference latency. Yet, their parallel decoding potential remains largely underexplored, as existing open-source models still require nearly token-length decoding steps to ensure performance. To address this, we introduce dParallel, a simple and effective method that unlocks the inherent parallelism of dLLMs for fast sampling. We identify that the key bottleneck to parallel decoding arises from the sequential certainty convergence for masked tokens. Building on this insight, we introduce the core of our approach: certainty-forcing distillation, a novel training strategy that distills the model to follow its original sampling trajectories while enforcing it to achieve high certainty on masked tokens more rapidly and in parallel. Extensive experiments across various benchmarks demonstrate that our method can dramatically reduce the number of decoding steps while maintaining performance. When applied to the LLaDA-8B-Instruct model, dParallel reduces decoding steps from 256 to 30 on GSM8K, achieving an 8.5x speedup without performance degradation. On the MBPP benchmark, it cuts decoding steps from 256 to 24, resulting in a 10.5x speedup while maintaining accuracy. Our code is available at https://github.com/czg1225/dParallel

