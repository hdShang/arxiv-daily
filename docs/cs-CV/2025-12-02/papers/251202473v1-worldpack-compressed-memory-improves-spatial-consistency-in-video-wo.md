---
layout: default
title: WorldPack: Compressed Memory Improves Spatial Consistency in Video World Modeling
---

# WorldPack: Compressed Memory Improves Spatial Consistency in Video World Modeling

**arXiv**: [2512.02473v1](https://arxiv.org/abs/2512.02473) | [PDF](https://arxiv.org/pdf/2512.02473.pdf)

**作者**: Yuta Oshima, Yusuke Iwasawa, Masahiro Suzuki, Yutaka Matsuo, Hiroki Furuta

---

## 💡 一句话要点

**提出WorldPack压缩内存模型以提升视频世界建模中的长期空间一致性**

**关键词**: `视频世界建模` `压缩内存` `空间一致性` `长期生成` `轨迹打包` `内存检索`

## 📋 核心要点

1. 核心问题：长上下文输入计算成本高，导致现有视频世界模型在长期时空一致性上表现不足
2. 方法要点：采用轨迹打包和内存检索的压缩内存机制，提高上下文效率并维持生成一致性
3. 实验或效果：在Minecraft的LoopNav基准测试中显著优于先进模型，验证了长期生成质量

## 📄 摘要（原文）

> Video world models have attracted significant attention for their ability to produce high-fidelity future visual observations conditioned on past observations and navigation actions. Temporally- and spatially-consistent, long-term world modeling has been a long-standing problem, unresolved with even recent state-of-the-art models, due to the prohibitively expensive computational costs for long-context inputs. In this paper, we propose WorldPack, a video world model with efficient compressed memory, which significantly improves spatial consistency, fidelity, and quality in long-term generation despite much shorter context length. Our compressed memory consists of trajectory packing and memory retrieval; trajectory packing realizes high context efficiency, and memory retrieval maintains the consistency in rollouts and helps long-term generations that require spatial reasoning. Our performance is evaluated with LoopNav, a benchmark on Minecraft, specialized for the evaluation of long-term consistency, and we verify that WorldPack notably outperforms strong state-of-the-art models.

