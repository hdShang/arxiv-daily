---
layout: default
title: "FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies"
---

# FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04996" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04996v1</a>
  <a href="https://arxiv.org/pdf/2509.04996.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04996v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04996v1', 'FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Moritz Reuss, Hongyi Zhou, Marcel Rühle, Ömer Erdinç Yağmurlu, Fabian Otto, Rudolf Lioutikov

**分类**: cs.RO

**发布日期**: 2025-09-05

**备注**: Published at CoRL 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://intuitive-robots.github.io/flower_vla/)

---

## 💡 一句话要点

**FLOWER：通过高效的视觉-语言-动作流策略实现通用机器人策略的大众化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作策略` `机器人学习` `扩散模型` `模型压缩` `中间模态融合` `Global-AdaLN` `通用机器人`

## 📋 核心要点

1. 现有基于扩散的视觉-语言-动作策略需要庞大的模型和数据集，计算成本高昂，阻碍了实际应用。
2. FLOWER通过中间模态融合和动作特定Global-AdaLN条件化，显著降低了模型参数量，提高了训练效率。
3. FLOWER在多个模拟和真实机器人任务中表现出与更大模型相当甚至更优的性能，并在CALVIN ABC基准上取得了新的SoTA。

## 📝 摘要（中文）

开发高效的视觉-语言-动作(VLA)策略对于实际机器人部署至关重要，但当前方法面临着过高的计算成本和资源需求。现有的基于扩散的VLA策略需要数十亿参数的模型和海量数据集才能实现强大的性能。本文通过两项贡献来应对这一效率挑战：中间模态融合，通过剪枝高达50%的LLM层来重新分配扩散头的容量；以及特定于动作的Global-AdaLN条件化，通过模块化自适应减少20%的参数。我们将这些进步整合到一个名为FLOWER的新型9.5亿参数VLA中。FLOWER仅用200个H100 GPU小时进行预训练，在跨越十个模拟和真实世界基准测试的190个任务中，提供了与更大的VLA相媲美的性能，并展示了跨不同机器人形态的鲁棒性。此外，FLOWER在CALVIN ABC基准测试中实现了4.53的新SoTA。演示、代码和预训练权重可在https://intuitive-robots.github.io/flower_vla/获得。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作(VLA)策略，特别是基于扩散模型的方法，通常需要数十亿参数的模型和大量数据进行训练，导致计算成本高昂，难以在资源有限的环境中部署。这些方法在模型规模和训练数据上的需求限制了其在实际机器人应用中的可行性。

**核心思路**：FLOWER的核心思路是通过更有效地利用模型参数和减少冗余计算来降低VLA策略的计算成本。具体而言，通过中间模态融合来减少LLM层的数量，并将模型容量重新分配给扩散头，以及通过动作特定的Global-AdaLN条件化来实现参数的模块化自适应，从而减少整体参数量。

**技术框架**：FLOWER的整体框架包含视觉编码器、语言编码器、中间模态融合模块、扩散模型和动作解码器。视觉和语言信息首先被编码，然后在中间模态融合模块中进行融合，该模块通过剪枝LLM层来减少参数。融合后的信息被输入到扩散模型中，该模型生成动作序列，最后由动作解码器将动作序列转换为具体的机器人控制指令。Global-AdaLN条件化模块用于根据不同的动作类型自适应地调整模型参数。

**关键创新**：FLOWER的关键创新在于中间模态融合和动作特定的Global-AdaLN条件化。中间模态融合通过剪枝LLM层，将模型容量重新分配给扩散头，从而在不损失性能的情况下减少了参数量。动作特定的Global-AdaLN条件化通过模块化自适应，允许模型根据不同的动作类型调整参数，进一步减少了参数量。

**关键设计**：FLOWER使用了一个9.5亿参数的VLA模型。中间模态融合中，LLM层被剪枝高达50%。Global-AdaLN条件化通过在AdaLN层中引入全局上下文信息来实现动作特定的参数调整。模型在200个H100 GPU小时内进行预训练。损失函数包括扩散模型的标准损失函数以及用于优化动作解码器的损失函数。

## 📊 实验亮点

FLOWER仅用9.5亿参数和200个H100 GPU小时的训练，在190个任务中实现了与更大VLA模型相媲美的性能。在CALVIN ABC基准测试中，FLOWER取得了4.53的新SoTA，证明了其在复杂机器人任务中的优越性能。实验结果表明，FLOWER在不同的机器人形态中具有良好的鲁棒性。

## 🎯 应用场景

FLOWER的潜在应用领域包括家庭服务机器人、工业自动化、医疗辅助机器人等。通过降低VLA策略的计算成本，FLOWER使得更广泛的机器人应用成为可能，尤其是在资源受限的环境中。该研究有望推动通用机器人策略的发展，使机器人能够更灵活地适应各种任务和环境。

## 📄 摘要（原文）

> Developing efficient Vision-Language-Action (VLA) policies is crucial for practical robotics deployment, yet current approaches face prohibitive computational costs and resource requirements. Existing diffusion-based VLA policies require multi-billion-parameter models and massive datasets to achieve strong performance. We tackle this efficiency challenge with two contributions: intermediate-modality fusion, which reallocates capacity to the diffusion head by pruning up to $50\%$ of LLM layers, and action-specific Global-AdaLN conditioning, which cuts parameters by $20\%$ through modular adaptation. We integrate these advances into a novel 950 M-parameter VLA called FLOWER. Pretrained in just 200 H100 GPU hours, FLOWER delivers competitive performance with bigger VLAs across $190$ tasks spanning ten simulation and real-world benchmarks and demonstrates robustness across diverse robotic embodiments. In addition, FLOWER achieves a new SoTA of 4.53 on the CALVIN ABC benchmark. Demos, code and pretrained weights are available at https://intuitive-robots.github.io/flower_vla/.

