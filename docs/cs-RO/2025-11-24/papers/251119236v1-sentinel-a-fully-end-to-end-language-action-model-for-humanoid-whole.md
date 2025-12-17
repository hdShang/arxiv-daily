---
layout: default
title: SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control
---

# SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control

**arXiv**: [2511.19236v1](https://arxiv.org/abs/2511.19236) | [PDF](https://arxiv.org/pdf/2511.19236.pdf)

**作者**: Yuxuan Wang, Haobin Jiang, Shiqing Yao, Ziluo Ding, Zongqing Lu

---

## 💡 一句话要点

**提出SENTINEL端到端语言-动作模型以解决人形机器人全身控制中语言与行为对齐问题**

**关键词**: `人形机器人控制` `端到端学习` `语言-动作映射` `流匹配` `全身控制` `多模态扩展`

## 📋 核心要点

1. 现有系统依赖遥操作或模块化管道，导致语言理解与物理执行分离
2. 模型直接映射语言命令和本体感觉输入到低级动作，使用流匹配生成动作块
3. 在仿真和真实部署中展示强语义理解和稳定执行，支持多模态扩展

## 📄 摘要（原文）

> Existing humanoid control systems often rely on teleoperation or modular generation pipelines that separate language understanding from physical execution. However, the former is entirely human-driven, and the latter lacks tight alignment between language commands and physical behaviors. In this paper, we present SENTINEL, a fully end-to-end language-action model for humanoid whole-body control. We construct a large-scale dataset by tracking human motions in simulation using a pretrained whole body controller, combined with their text annotations. The model directly maps language commands and proprioceptive inputs to low-level actions without any intermediate representation. The model generates action chunks using flow matching, which can be subsequently refined by a residual action head for real-world deployment. Our method exhibits strong semantic understanding and stable execution on humanoid robots in both simulation and real-world deployment, and also supports multi-modal extensions by converting inputs into texts.

