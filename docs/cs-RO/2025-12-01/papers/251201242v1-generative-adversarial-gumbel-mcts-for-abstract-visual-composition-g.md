---
layout: default
title: Generative Adversarial Gumbel MCTS for Abstract Visual Composition Generation
---

# Generative Adversarial Gumbel MCTS for Abstract Visual Composition Generation

**arXiv**: [2512.01242v1](https://arxiv.org/abs/2512.01242) | [PDF](https://arxiv.org/pdf/2512.01242.pdf)

**作者**: Zirui Zhao, Boye Niu, David Hsu, Wee Sun Lee

---

## 💡 一句话要点

**提出约束引导框架结合几何推理与神经语义，用于抽象视觉组合生成。**

**关键词**: `抽象视觉组合` `几何约束` `蒙特卡洛树搜索` `视觉语言模型` `对抗奖励优化` `Tangram Assembly`

## 📋 核心要点

1. 核心问题：抽象视觉组合在几何约束和模糊目标下，因组合放置、数据有限和离散可行性而难以生成。
2. 方法要点：结合AlphaGo式搜索确保可行性，微调视觉语言模型评分语义对齐，并利用对抗奖励优化。
3. 实验或效果：在Tangram Assembly任务中，比扩散和自回归基线在约束收紧时具有更高有效性和语义保真度。

## 📄 摘要（原文）

> We study abstract visual composition, in which identity is primarily determined by the spatial configuration and relations among a small set of geometric primitives (e.g., parts, symmetry, topology). They are invariant primarily to texture and photorealistic detail. Composing such structures from fixed components under geometric constraints and vague goal specification (such as text) is non-trivial due to combinatorial placement choices, limited data, and discrete feasibility (overlap-free, allowable orientations), which create a sparse solution manifold ill-suited to purely statistical pixel-space generators. We propose a constraint-guided framework that combines explicit geometric reasoning with neural semantics. An AlphaGo-style search enforces feasibility, while a fine-tuned vision-language model scores semantic alignment as reward signals. Our algorithm uses a policy network as a heuristic in Monte-Carlo Tree Search and fine-tunes the network via search-generated plans. Inspired by the Generative Adversarial Network, we use the generated instances for adversarial reward refinement. Over time, the generation should approach the actual data more closely when the reward model cannot distinguish between generated instances and ground-truth. In the Tangram Assembly task, our approach yields higher validity and semantic fidelity than diffusion and auto-regressive baselines, especially as constraints tighten.

