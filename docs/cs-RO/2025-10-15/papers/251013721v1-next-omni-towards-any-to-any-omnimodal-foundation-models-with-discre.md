---
layout: default
title: NExT-OMNI: Towards Any-to-Any Omnimodal Foundation Models with Discrete Flow Matching
---

# NExT-OMNI: Towards Any-to-Any Omnimodal Foundation Models with Discrete Flow Matching

**arXiv**: [2510.13721v1](https://arxiv.org/abs/2510.13721) | [PDF](https://arxiv.org/pdf/2510.13721.pdf)

**作者**: Run Luo, Xiaobo Xia, Lu Wang, Longze Chen, Renke Shan, Jing Luo, Min Yang, Tat-Seng Chua

---

## 💡 一句话要点

**提出NExT-OMNI模型，通过离散流匹配实现任意模态间理解与生成**

**关键词**: `多模态基础模型` `离散流匹配` `任意模态生成` `跨模态检索` `统一建模`

## 📋 核心要点

1. 现有自回归模型难以平衡理解与生成能力，限制多模态应用
2. 采用离散流范式统一建模，支持高效任意模态转换与交互
3. 在大规模数据训练下，在多轮交互和跨模态检索中表现优异

## 📄 摘要（原文）

> Next-generation multimodal foundation models capable of any-to-any
> cross-modal generation and multi-turn interaction will serve as core components
> of artificial general intelligence systems, playing a pivotal role in
> human-machine interaction. However, most existing multimodal models remain
> constrained by autoregressive architectures, whose inherent limitations prevent
> a balanced integration of understanding and generation capabilities. Although
> hybrid and decoupling strategies have been explored to address these tasks
> within unified frameworks separately, their redundant, non-integrated designs
> limit their applicability to broader scenarios, such as cross-modal
> retrieval.In this work, we introduce NExT-OMNI, an open-source omnimodal
> foundation model that achieves unified modeling through discrete flow
> paradigms. By leveraging metric-induced probability paths and kinetic optimal
> velocities, NExT-OMNI natively supports any-to-any understanding and generation
> with enhanced response efficiency, while enabling broader application scenarios
> through concise unified representations rather than task-decoupled designs.
> Trained on large-scale interleaved text, image, video, and audio data,
> NExT-OMNI delivers competitive performance on multimodal generation and
> understanding benchmarks, while outperforming prior unified models in
> multi-turn multimodal interaction and cross-modal retrieval, highlighting its
> architectural advantages as a next-generation multimodal foundation model. To
> advance further research, we release training details, data protocols, and
> open-source both the code and model checkpoints.

