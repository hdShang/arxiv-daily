---
layout: default
title: KlingAvatar 2.0 Technical Report
---

# KlingAvatar 2.0 Technical Report

**arXiv**: [2512.13313v1](https://arxiv.org/abs/2512.13313) | [PDF](https://arxiv.org/pdf/2512.13313.pdf)

**作者**: Kling Team, Jialu Chen, Yikang Ding, Zhixue Fang, Kun Gai, Yuan Gao, Kang He, Jingyun Hua, Boyuan Jiang, Mingming Lao, Xiaohan Li, Hui Liu, Jiwen Liu, Xiaoqiang Liu, Yuan Liu, Shun Lu, Yongsen Mao, Yingchao Shao, Huafeng Shi, Xiaoyu Shi, Peiqin Sun, Songlin Tang, Pengfei Wan, Chao Wang, Xuebo Wang, Haoxian Zhang, Yuanxing Zhang, Yan Zhou

---

## 💡 一句话要点

**提出KlingAvatar 2.0时空级联框架以解决长时高分辨率虚拟形象视频生成中的效率与对齐问题**

**关键词**: `虚拟形象视频生成` `时空级联框架` `长时高分辨率视频` `跨模态指令对齐` `身份控制`

## 📋 核心要点

1. 核心问题：现有方法在生成长时高分辨率视频时存在效率低、时间漂移、质量下降和提示跟随弱的问题
2. 方法要点：采用时空级联框架，先生成低分辨率蓝图关键帧，再通过首尾帧策略细化成高分辨率子片段，并引入Co-Reasoning Director增强跨模态指令对齐
3. 实验或效果：模型在长时高分辨率视频生成中表现出增强的视觉清晰度、逼真的唇齿渲染、强身份保持和连贯的多模态指令跟随

## 📄 摘要（原文）

> Avatar video generation models have achieved remarkable progress in recent years. However, prior work exhibits limited efficiency in generating long-duration high-resolution videos, suffering from temporal drifting, quality degradation, and weak prompt following as video length increases. To address these challenges, we propose KlingAvatar 2.0, a spatio-temporal cascade framework that performs upscaling in both spatial resolution and temporal dimension. The framework first generates low-resolution blueprint video keyframes that capture global semantics and motion, and then refines them into high-resolution, temporally coherent sub-clips using a first-last frame strategy, while retaining smooth temporal transitions in long-form videos. To enhance cross-modal instruction fusion and alignment in extended videos, we introduce a Co-Reasoning Director composed of three modality-specific large language model (LLM) experts. These experts reason about modality priorities and infer underlying user intent, converting inputs into detailed storylines through multi-turn dialogue. A Negative Director further refines negative prompts to improve instruction alignment. Building on these components, we extend the framework to support ID-specific multi-character control. Extensive experiments demonstrate that our model effectively addresses the challenges of efficient, multimodally aligned long-form high-resolution video generation, delivering enhanced visual clarity, realistic lip-teeth rendering with accurate lip synchronization, strong identity preservation, and coherent multimodal instruction following.

