---
layout: default
title: "Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies"
---

# Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20072" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20072v3</a>
  <a href="https://arxiv.org/pdf/2508.20072.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20072v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20072v3', 'Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhixuan Liang, Yizhuo Li, Tianshuo Yang, Chengyue Wu, Sitong Mao, Tian Nian, Liuao Pei, Shunbo Zhou, Xiaokang Yang, Jiangmiao Pang, Yao Mu, Ping Luo

**分类**: cs.CV, cs.LG, cs.RO

**发布日期**: 2025-08-27 (更新: 2025-12-22)

**备注**: New experiments on VL retention and new ablations. 18 pages

**🔗 代码/项目**: [GITHUB](https://github.com/Liang-ZX/DiscreteDiffusionVLA/tree)

---

## 💡 一句话要点

**提出离散扩散VLA以解决视觉-语言-动作模型的统一性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `离散扩散` `自适应解码` `机器人控制` `多模态学习`

## 📋 核心要点

1. 现有的视觉-语言-动作模型在生成动作时存在固定顺序和信息路径碎片化的问题，限制了模型的统一性和扩展性。
2. 本文提出离散扩散VLA，通过离散扩散建模动作块，支持自适应解码顺序和二次重掩蔽，提升了动作建模的精确性。
3. 实验结果表明，离散扩散VLA在LIBERO上达到了96.3%的平均成功率，优于自回归和MLP解码器，展示了更强的视觉-语言能力保留。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型将大型视觉-语言骨干网络适配于将图像和指令映射为机器人动作。然而，现有的VLA模型通常采用固定的自回归生成顺序或在骨干网络外附加独立的MLP或扩散头，导致信息路径碎片化和训练要求专门化，从而阻碍了统一且可扩展的架构。本文提出了离散扩散VLA，一种统一的变换器策略，通过离散扩散建模离散化的动作块。该设计保留了扩散的渐进精炼范式，同时与VLM的离散令牌接口原生兼容。我们的方案实现了自适应解码顺序，先解决简单动作元素，再处理复杂元素，并通过二次重掩蔽在精炼轮次中重新审视不确定的预测，从而提高一致性并实现稳健的错误修正。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉-语言-动作模型在动作生成时的固定顺序和信息碎片化问题，这些问题限制了模型的统一性和扩展性。

**核心思路**：提出离散扩散VLA，通过离散化的动作块建模，采用自适应解码顺序和二次重掩蔽策略，以提高动作生成的精确性和一致性。

**技术框架**：整体架构为统一的变换器策略，包含离散扩散模块和自适应解码机制，支持并行解码，打破自回归瓶颈。

**关键创新**：最重要的技术创新在于将离散扩散引入VLA模型，允许模型在解码过程中动态调整顺序，并通过重掩蔽机制增强预测的准确性。

**关键设计**：在模型设计中，采用了离散令牌接口，设置了适应性损失函数，并优化了网络结构以支持高效的并行处理。实验中还进行了消融研究，以验证视觉-语言能力的保留。

## 📊 实验亮点

离散扩散VLA在LIBERO数据集上达到了96.3%的平均成功率，在SimplerEnv-Fractal上实现了71.2%的视觉匹配率，整体在SimplerEnv-Bridge上达到了54.2%。这些结果显著优于自回归、MLP解码器和连续扩散基线，展示了模型在动作建模和训练一致性方面的优势。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动化系统和人机交互等。通过提升视觉-语言-动作模型的统一性和扩展性，未来可在更大规模的数据集和模型中实现更复杂的任务，推动智能系统的发展。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models adapt large vision-language backbones to map images and instructions into robot actions. However, prevailing VLAs either generate actions auto-regressively in a fixed left-to-right order or attach separate MLP or diffusion heads outside the backbone, leading to fragmented information pathways and specialized training requirements that hinder a unified, scalable architecture. We present Discrete Diffusion VLA, a unified-transformer policy that models discretized action chunks with discrete diffusion. The design retains diffusion's progressive refinement paradigm while remaining natively compatible with the discrete token interface of VLMs. Our method achieves an adaptive decoding order that resolves easy action elements before harder ones and uses secondary re-masking to revisit uncertain predictions across refinement rounds, which improves consistency and enables robust error correction. This unified decoder preserves pre-trained vision-language priors, supports parallel decoding, breaks the autoregressive bottleneck, and reduces the number of function evaluations. Discrete Diffusion VLA achieves 96.3% avg. success rates on LIBERO, 71.2% visual matching on SimplerEnv-Fractal and 54.2% overall on SimplerEnv-Bridge. We also provide ablation study on vision-language ability retention on LIBERO-OOD (Out-of-Distribution) benchmark, with our method improving over autoregressive, MLP decoder and continuous diffusion baselines. These findings indicate that discrete-diffusion VLA supports precise action modeling and consistent training, laying groundwork for scaling VLA to larger models and datasets. Our code is available at https://github.com/Liang-ZX/DiscreteDiffusionVLA/tree/libero.

