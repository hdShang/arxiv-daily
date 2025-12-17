---
layout: default
title: OTSNet: A Neurocognitive-Inspired Observation-Thinking-Spelling Pipeline for Scene Text Recognition
---

# OTSNet: A Neurocognitive-Inspired Observation-Thinking-Spelling Pipeline for Scene Text Recognition

**arXiv**: [2511.08133v1](https://arxiv.org/abs/2511.08133) | [PDF](https://arxiv.org/pdf/2511.08133.pdf)

**作者**: Lixu Sun, Nurmemet Yolwas, Wushour Silamu

---

## 💡 一句话要点

**提出OTSNet以解决场景文本识别中视觉-语言跨模态对齐问题**

**关键词**: `场景文本识别` `跨模态对齐` `神经认知启发` `注意力机制` `多模态融合` `不规则文本处理`

## 📋 核心要点

1. 核心问题：现有方法视觉-语言解耦优化导致错误传播，视觉编码器注意力偏向背景干扰，解码器空间对齐差
2. 方法要点：采用观察-思考-拼写三阶段管道，集成双注意力编码器、位置感知模块和多模态验证器
3. 实验或效果：在Union14M-L和OST数据集上达到83.5%和79.1%准确率，14个场景中9个创纪录

## 📄 摘要（原文）

> Scene Text Recognition (STR) remains challenging due to real-world complexities, where decoupled visual-linguistic optimization in existing frameworks amplifies error propagation through cross-modal misalignment. Visual encoders exhibit attention bias toward background distractors, while decoders suffer from spatial misalignment when parsing geometrically deformed text-collectively degrading recognition accuracy for irregular patterns. Inspired by the hierarchical cognitive processes in human visual perception, we propose OTSNet, a novel three-stage network embodying a neurocognitive-inspired Observation-Thinking-Spelling pipeline for unified STR modeling. The architecture comprises three core components: (1) a Dual Attention Macaron Encoder (DAME) that refines visual features through differential attention maps to suppress irrelevant regions and enhance discriminative focus; (2) a Position-Aware Module (PAM) and Semantic Quantizer (SQ) that jointly integrate spatial context with glyph-level semantic abstraction via adaptive sampling; and (3) a Multi-Modal Collaborative Verifier (MMCV) that enforces self-correction through cross-modal fusion of visual, semantic, and character-level features. Extensive experiments demonstrate that OTSNet achieves state-of-the-art performance, attaining 83.5% average accuracy on the challenging Union14M-L benchmark and 79.1% on the heavily occluded OST dataset-establishing new records across 9 out of 14 evaluation scenarios.

